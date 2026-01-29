#!/usr/bin/env python3
"""
Agent Orchestrator
Manages multiple agents, routes messages, coordinates research
Like Clawed/Moltbot but for penetration testing
Author: SHAdd0WTAka
"""

import asyncio
from typing import Dict, List, Optional, Any
from datetime import datetime
import logging

from .agent_base import BaseAgent, AgentMessage, AgentRole

logger = logging.getLogger("ZenAI.Agents")


class AgentOrchestrator:
    """
    Central coordinator for multi-agent system
    Manages agent lifecycle, message routing, and context sharing
    """
    
    def __init__(self, zen_orchestrator=None):
        self.agents: Dict[str, BaseAgent] = {}
        self.agent_by_role: Dict[AgentRole, List[BaseAgent]] = {}
        self.shared_context: Dict[str, Any] = {}
        self.message_history: List[AgentMessage] = []
        self.conversation_threads: Dict[str, List[str]] = {}  # thread_id -> message_ids
        self.zen_orchestrator = zen_orchestrator  # Link to LLM orchestrator
        self.running = False
        self.research_coordination: Dict[str, Any] = {}
        
    def register_agent(self, agent: BaseAgent):
        """Register an agent with the orchestrator"""
        self.agents[agent.id] = agent
        agent.orchestrator = self
        
        # Index by role
        if agent.role not in self.agent_by_role:
            self.agent_by_role[agent.role] = []
        self.agent_by_role[agent.role].append(agent)
        
        logger.info(f"[Orchestrator] Registered agent {agent.name} ({agent.role.value})")
        
    def unregister_agent(self, agent_id: str):
        """Remove an agent from the system"""
        if agent_id in self.agents:
            agent = self.agents[agent_id]
            
            # Remove from role index
            if agent.role in self.agent_by_role:
                self.agent_by_role[agent.role] = [
                    a for a in self.agent_by_role[agent.role] 
                    if a.id != agent_id
                ]
                
            del self.agents[agent_id]
            logger.info(f"[Orchestrator] Unregistered agent {agent_id}")
            
    async def route_message(self, msg: AgentMessage):
        """Route a message to the appropriate recipient(s)"""
        self.message_history.append(msg)
        
        if msg.recipient == "all":
            # Broadcast to all agents except sender
            for agent_id, agent in self.agents.items():
                if f"[{agent_id}]" not in msg.sender:
                    await agent.receive_message(msg)
                    
        elif msg.recipient.startswith("role:"):
            # Send to all agents of a specific role
            role_str = msg.recipient.split(":")[1]
            try:
                role = AgentRole(role_str)
                for agent in self.agent_by_role.get(role, []):
                    if f"[{agent.id}]" not in msg.sender:
                        await agent.receive_message(msg)
            except ValueError:
                logger.error(f"[Orchestrator] Invalid role: {role_str}")
                
        else:
            # Direct message to specific agent
            # Parse agent ID from recipient string like "AgentName[ID]"
            if "[" in msg.recipient and "]" in msg.recipient:
                agent_id = msg.recipient.split("[")[1].split("]")[0]
                if agent_id in self.agents:
                    await self.agents[agent_id].receive_message(msg)
                    
    async def update_shared_context(self, key: str, value: Any, source_agent_id: str):
        """Update shared context and notify all agents"""
        self.shared_context[key] = {
            "value": value,
            "updated_by": source_agent_id,
            "timestamp": datetime.now().isoformat()
        }
        
        # Notify all agents of context update
        for agent_id, agent in self.agents.items():
            if agent_id != source_agent_id:
                await agent.receive_message(AgentMessage(
                    sender="orchestrator",
                    recipient=f"{agent.name}[{agent.id}]",
                    msg_type="context_update",
                    content=f"Context updated: {key}",
                    context={"key": key, "value": value}
                ))
                
    def get_shared_context(self, key: str = None) -> Any:
        """Get value from shared context"""
        if key:
            return self.shared_context.get(key, {}).get("value")
        return self.shared_context
        
    async def start_research_coordination(self, topic: str, 
                                         pentest_context: Dict) -> str:
        """
        Coordinate multi-agent research on a topic
        Returns thread ID for tracking
        """
        thread_id = f"research_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        
        self.research_coordination[thread_id] = {
            "topic": topic,
            "context": pentest_context,
            "started": datetime.now().isoformat(),
            "agents_involved": [],
            "findings": [],
            "status": "active"
        }
        
        # Notify all research agents
        for agent in self.agent_by_role.get(AgentRole.RESEARCHER, []):
            await agent.receive_message(AgentMessage(
                sender="orchestrator",
                recipient=f"{agent.name}[{agent.id}]",
                msg_type="research_task",
                content=f"Research coordination started: {topic}",
                context={
                    "thread_id": thread_id,
                    "pentest_context": pentest_context,
                    "shared_context": self.shared_context
                },
                priority=3
            ))
            self.research_coordination[thread_id]["agents_involved"].append(agent.id)
            
        logger.info(f"[Orchestrator] Started research coordination: {thread_id}")
        return thread_id
        
    async def coordinate_agents(self, task_type: str, context: Dict) -> Dict:
        """
        Coordinate multiple agents for a complex task
        Agents will communicate and share findings
        """
        results = {
            "task_type": task_type,
            "started": datetime.now().isoformat(),
            "agent_responses": {}
        }
        
        # Determine which agents to involve based on task
        involved_roles = []
        
        if task_type == "reconnaissance":
            involved_roles = [AgentRole.RESEARCHER, AgentRole.ANALYST]
        elif task_type == "vulnerability_analysis":
            involved_roles = [AgentRole.ANALYST, AgentRole.EXPLOIT]
        elif task_type == "exploit_development":
            involved_roles = [AgentRole.EXPLOIT, AgentRole.ANALYST]
        elif task_type == "full_assessment":
            involved_roles = [AgentRole.RESEARCHER, AgentRole.ANALYST, AgentRole.EXPLOIT]
            
        # Start all involved agents
        tasks = []
        for role in involved_roles:
            for agent in self.agent_by_role.get(role, []):
                agent_task = asyncio.create_task(
                    agent.execute_task({
                        "type": task_type,
                        "context": context,
                        "shared_context": self.shared_context
                    })
                )
                tasks.append((agent.id, agent_task))
                
        # Wait for all agents to complete
        for agent_id, task in tasks:
            try:
                result = await asyncio.wait_for(task, timeout=300)
                results["agent_responses"][agent_id] = result
            except asyncio.TimeoutError:
                results["agent_responses"][agent_id] = {"error": "timeout"}
                
        # Agents should have communicated with each other during execution
        # Collect their findings from shared context
        results["shared_findings"] = self.shared_context
        results["completed"] = datetime.now().isoformat()
        
        return results
        
    async def facilitate_conversation(self, topic: str, 
                                     participants: List[str],
                                     rounds: int = 3) -> List[AgentMessage]:
        """
        Facilitate a multi-round conversation between agents
        Similar to Clawed/Moltbot group discussions
        """
        conversation = []
        
        for round_num in range(rounds):
            logger.info(f"[Orchestrator] Conversation round {round_num + 1}/{rounds}")
            
            for participant_id in participants:
                if participant_id in self.agents:
                    agent = self.agents[participant_id]
                    
                    # Request agent's thoughts on topic
                    msg = AgentMessage(
                        sender="orchestrator",
                        recipient=f"{agent.name}[{agent.id}]",
                        msg_type="conversation_round",
                        content=f"Round {round_num + 1}: Share your thoughts on {topic}",
                        context={
                            "round": round_num + 1,
                            "topic": topic,
                            "conversation_so_far": [m.to_dict() for m in conversation],
                            "shared_context": self.shared_context
                        },
                        requires_response=True
                    )
                    
                    await agent.receive_message(msg)
                    
        return conversation
        
    async def start_all(self):
        """Start all registered agents"""
        self.running = True
        for agent in self.agents.values():
            await agent.start()
            
    async def stop_all(self):
        """Stop all agents gracefully"""
        self.running = False
        for agent in self.agents.values():
            await agent.stop()
            
    def get_system_status(self) -> Dict:
        """Get status of entire multi-agent system"""
        return {
            "agents": {
                agent_id: agent.get_status()
                for agent_id, agent in self.agents.items()
            },
            "shared_context_keys": list(self.shared_context.keys()),
            "message_count": len(self.message_history),
            "active_research": list(self.research_coordination.keys()),
            "role_distribution": {
                role.value: len(agents)
                for role, agents in self.agent_by_role.items()
            }
        }
