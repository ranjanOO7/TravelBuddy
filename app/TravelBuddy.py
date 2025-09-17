from crewai import Crew,Agent,Task
from crewai.project import CrewBase,agent,crew,task
import LLM

llm = LLM.get_llm()

@CrewBase
class TravelBuddy():
    "This the Travel buddy Agentic solution. This will provide you a complete itinerary for a destination."

    agents_config = "config/agents.yml"
    tasks_config = "config/tasks.yml"

    @agent
    def travelling_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["travelling_agent"],
            llm=llm
        )

    @agent
    def itinerary_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["itinerary_agent"],
            llm=llm
        )

    @task
    def gather_information_task(self) -> Task:
        return Task(
            config=self.tasks_config["gather_information_task"],
            agent=self.travelling_agent()
        )

    @task
    def itinerary_planner(self) -> Task:
        return Task(
            config=self.tasks_config["itinerary_planner"],
            agent=self.itinerary_agent()
        )

    @crew
    def travelBuddyCrew(self) -> Crew:
        return Crew(
            agents=[self.travelling_agent(), self.itinerary_agent()],
            tasks=[self.gather_information_task(), self.itinerary_planner()],
            verbose=True
        )

inputs = {
    "destination":"Mumbai",
    "days":"2"
}

if __name__ == "__main__":
    travelBuddy = TravelBuddy()
    response = travelBuddy.travelBuddyCrew().kickoff(inputs=inputs)
    print(response)