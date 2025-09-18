from crewai import Crew,Agent,Task
from crewai.project import CrewBase,agent,task,crew
from dotenv import load_dotenv
import LLM

llm = LLM.get_llm()

load_dotenv()

@CrewBase
class FlightAgent:
    """This Purpose of this agent is to assist in flight searching and booking."""

    agents_config = "config/travel/agents.yml"
    tasks_config = "config/travel/tasks.yml"

    @agent
    def flight_finder_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["flight_finder_agent"],
            llm=llm,
        )

    @task
    def flight_search_task(self) -> Task:
        return Task(
            config=self.tasks_config["flight_search_task"],
            agent=self.flight_finder_agent(),
        )

    @crew
    def flight_crew_agent(self) -> Crew:
        return Crew(
            agents=[self.flight_finder_agent()],
            tasks=[self.flight_search_task()],
            verbose=True
        )


inputs={
    "source":"Bengaluru",
    "destination":"Bhubaneshwar",
    "date":"15th Dec 2025"
}

if __name__ == "__main__":
    flight_agent = FlightAgent()
    response = flight_agent.flight_crew_agent().kickoff(inputs=inputs)
    print(response)