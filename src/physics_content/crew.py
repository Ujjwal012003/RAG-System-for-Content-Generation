"""
Physics Content Generation Crew
Uses RAG-Anything to generate content from processed chapters
NO external search tools - purely RAG-based
"""

from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import CodeInterpreterTool, SerperDevTool
from typing import List
import os
import sys
from pathlib import Path

# Add physics_content directory to Python path
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

os.environ["CREWAI_AGENTS_CONFIG"] = "src/physics_content/config/agents.yaml"
os.environ["CREWAI_TASKS_CONFIG"] = "src/physics_content/config/tasks.yaml"


@CrewBase
class PhysicsContentCrew():
    """
    Physics Content crew with RAG-powered generation
    All agents use PhysicsRAGTool to query processed chapters
    NO internet search tools used
    """
    
    agents: List[BaseAgent]
    tasks: List[Task]
    
    def __init__(self):
        """Initialize crew with RAG tool and SerperDev tool"""
        print("\n" + "="*80)
        print("🚀 INITIALIZING PHYSICS CONTENT GENERATION CREW")
        print("="*80)
        
        
        # Initialize RAG tool once for all agents
        try:
            # Import from current directory's tools folder
            from tools.custom_tool import PhysicsRAGTool
            self.rag_tool = PhysicsRAGTool()
            print("✅ RAG Tool initialized successfully!")
            print("📚 Data Source: Processed chapters in rag_storage/lightrag/")
            print("🔍 Retrieval Mode: Hybrid (local + global)")
        except Exception as e:
            print(f"❌ RAG Tool initialization failed: {e}")
            print(f"⚠️ Import error details: {type(e).__name__}")
            print(f"⚠️ Current directory: {current_dir}")
            print("⚠️ Crew will run without RAG access (not recommended)")
            self.rag_tool = None
        
        # Initialize SerperDev tool for NCERT TOC verification
        try:
            self.serper_tool = SerperDevTool()
            print("✅ SerperDev Tool initialized successfully!")
            print("🌐 Web Search: ENABLED for NCERT TOC verification")
        except Exception as e:
            print(f"⚠️ SerperDev Tool initialization failed: {e}")
            print("⚠️ Web search disabled - using RAG-only mode")
            self.serper_tool = None
        
        print("="*80 + "\n")
    
    @agent
    def research_agent(self) -> Agent:
        """Research agent with RAG access to processed chapters"""
        tools = [self.rag_tool] if self.rag_tool else []
        return Agent(
            config=self.agents_config['research_agent'],
            verbose=True,
            tools=tools,
            allow_delegation=False,
            
        )
    
    @agent
    def content_indexer(self) -> Agent:
        """Content indexer with RAG + SerperDev for NCERT TOC verification"""
        tools = []
        if self.rag_tool:
            tools.append(self.rag_tool)
        if self.serper_tool:
            tools.append(self.serper_tool)
        return Agent(
            config=self.agents_config['content_indexer'],
            verbose=True,
            tools=tools,
            allow_delegation=False,
           
        )
    
    @agent
    def content_generator(self) -> Agent:
        """Content generator with RAG access"""
        tools = [self.rag_tool] if self.rag_tool else []
        return Agent(
            config=self.agents_config['content_generator'],
            verbose=True,
            tools=tools,
            allow_delegation=False,
            
        )
    
    @agent
    def rag_enhancer(self) -> Agent:
        """RAG enhancer with RAG + SerperDev for topic verification"""
        tools = []
        if self.rag_tool:
            tools.append(self.rag_tool)
        if self.serper_tool:
            tools.append(self.serper_tool)
        return Agent(
            config=self.agents_config['rag_enhancer'],
            verbose=True,
            tools=tools,
            allow_delegation=False,
            
        )
    

    @agent
    def markdown_formatter(self) -> Agent:
        """Markdown formatter with code interpreter (no RAG needed)"""
        return Agent(
            config=self.agents_config['markdown_formatter'],
            verbose=True,
            tools=[CodeInterpreterTool()],
            allow_delegation=False,
            
        )
    
    # Tasks configuration
    @task
    def research_physics_chapter(self) -> Task:
        return Task(
            config=self.tasks_config['research_physics_chapter']
        )
    
    @task
    def create_topic_index(self) -> Task:
        return Task(
            config=self.tasks_config['create_topic_index']
        )
    
    @task
    def generate_detailed_content(self) -> Task:
        return Task(
            config=self.tasks_config['generate_detailed_content']
        )
    
    @task
    def enhance_with_rag(self) -> Task:
        return Task(
            config=self.tasks_config['enhance_with_rag']
        )
    

    
    @task
    def create_final_markdown(self) -> Task:
        return Task(
            config=self.tasks_config['create_final_markdown'],
            output_file='class_12_physics_chapter_{chapter_number}_{chapter_name}.md'
        )
    
    @crew
    def crew(self) -> Crew:
        """Create crew with sequential processing"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )
