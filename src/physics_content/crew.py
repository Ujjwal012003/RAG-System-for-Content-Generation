from crewai import Agent, Crew, Process, Task
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from crewai_tools import SerperDevTool, ScrapeWebsiteTool, CodeInterpreterTool
from typing import List
import os

os.environ["CREWAI_AGENTS_CONFIG"] = "src/physics_content/config/agents.yaml"
os.environ["CREWAI_TASKS_CONFIG"]  = "src/physics_content/config/tasks.yaml"

@CrewBase
class PhysicsContentCrew():
    """Physics Content crew with briefed contexts, per-section generation, and file-based handoff"""
    agents: List[BaseAgent]
    tasks: List[Task]

    # ... (agents remain the same) ...

    @agent
    def research_agent(self) -> Agent:
        return Agent(config=self.agents_config['research_agent'], verbose=True)

    @agent
    def content_indexer(self) -> Agent:
        return Agent(config=self.agents_config['content_indexer'], verbose=True,
                     tools=[SerperDevTool(), ScrapeWebsiteTool()])

    @agent
    def content_generator(self) -> Agent:
        try:
            from physics_content.rag_system import get_rag_tool
            rag_tool = get_rag_tool()
            print("✅ RAG tool loaded for content generator!")
            return Agent(config=self.agents_config['content_generator'], 
                        verbose=True, tools=[rag_tool])
        except Exception as e:
            print(f"⚠️ RAG tool loading failed for content generator: {e}")
            return Agent(config=self.agents_config['content_generator'], verbose=True)

    @agent
    def quality_reviewer(self) -> Agent:
        return Agent(config=self.agents_config['quality_reviewer'], verbose=True)

    @agent
    def rag_enhancer(self) -> Agent:
        try:
            from .rag_system import get_rag_tool
            rag_tool = get_rag_tool()
            print("✅ RAG Enhancement Tool loaded successfully!")
            return Agent(config=self.agents_config['rag_enhancer'], verbose=True,
                         tools=[rag_tool])
        except Exception as e:
            print(f"⚠️ RAG tool loading failed: {e}")
            print("🔄 Using agent without tools as fallback")
            return Agent(config=self.agents_config['rag_enhancer'], verbose=True)

    @agent
    def markdown_formatter(self) -> Agent:
        return Agent(config=self.agents_config['markdown_formatter'], verbose=True,
                     tools=[CodeInterpreterTool()])

    # --- Corrected Task Order ---

    @task
    def research_physics_chapter(self) -> Task:
        return Task(
            config=self.tasks_config['research_physics_chapter'],
            output_dir='artifacts/research/{chapter_number}',
            output_file='artifacts/research/{chapter_number}/research_brief.md'
        )

    @task
    def create_topic_index(self) -> Task:
        return Task(
            config=self.tasks_config['create_topic_index'],
            output_dir='artifacts/index/{chapter_number}',
            output_file='artifacts/index/{chapter_number}/index.md'
        )

    @task
    def generate_detailed_content(self) -> Task:
        return Task(
            config=self.tasks_config['generate_detailed_content'],
            output_dir='artifacts/content/{chapter_number}'
        )

    @task
    def enhance_with_rag(self) -> Task:
        return Task(
            config=self.tasks_config['enhance_with_rag'],
            output_dir='artifacts/enhanced/{chapter_number}'
        )

    @task
    def review_content_quality(self) -> Task:
        return Task(
            config=self.tasks_config['review_content_quality'],
            output_dir='artifacts/content/{chapter_number}'
        )

    @task
    def create_final_markdown(self) -> Task:
        return Task(
            config=self.tasks_config['create_final_markdown'],
            output_file='class_12_physics_chapter_{chapter_number}_{chapter_name}.md'
        )

    @crew
    def crew(self) -> Crew:
        print("Loaded task keys:", list(self.tasks_config.keys()))
        print("Loaded agent keys:", list(self.agents_config.keys()))
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )