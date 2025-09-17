# TravelBuddy 🛫

TravelBuddy is a Streamlit-powered AI travel planner that leverages CrewAI agents to generate personalized travel itineraries based on user inputs such as destination and trip duration. This project combines the power of autonomous AI agents with an easy-to-use web interface for a seamless trip planning experience.

---

## Features

- Interactive Streamlit UI for inputting travel destination and number of days.
- Multi-agent orchestration using CrewAI for research and itinerary planning.
- AI-generated, well-structured itinerary output.
- Configurable agents and tasks through YAML files.
- Easy environment configuration and API key management via `.env` file.

---

## Setup Instructions

### Prerequisites
- Python 3.10+
- Git (optional, for cloning)

### Installation Steps

1. **Clone the repository** (or download source code):


2. **Create and activate a virtual environment:**
- Windows CMD:
  ```
  python -m venv .venv
  .venv\Scripts\activate.bat
  ```
- PowerShell:
  ```
  python -m venv .venv
  .venv\Scripts\Activate.ps1
  ```
- macOS/Linux:
  ```
  python3 -m venv .venv
  source .venv/bin/activate
  ```

3. **Install the required dependencies:**
    ```
    pip install streamlit crewai python-dotenv
    ```

4. **Add your API key(s) in a `.env` file at the project root:**
    ```
   GROQ_API_KEY=your_groq_api_key_here
   ```
   
> **Important:** Keep `.env` secret and never commit it to source control.

5. **Configure agents and tasks (optional):**  
Modify `config/agents.yml` and `config/tasks.yml` to customize agent roles, prompts, and task flows.

---

## Running the Application

1. Make sure your virtual environment is activated.

2. Run the Streamlit app:
    ```
   streamlit run app/main.py
   ```
   
3. Open your web browser and navigate to the provided URL, normally:  

    `http://localhost:8501`


4. Enter the destination and number of days on the form, then submit to receive your AI-generated travel itinerary.

---

## Notes

- Ensure your API key is valid and added in `.env` for the app to function.
- YAML files allow easy customization of agent behavior without changing code.
- The app uses CrewAI for multi-agent coordination and Groq-powered LLMs for natural language generation.
- Streamlit offers a lightweight web UI enabling quick interactions.

---

## License

This repository is provided for educational and personal use only.  
For commercial or production applications, make sure to add an appropriate license.

---

Enjoy your automated travel planning with **TravelBuddy**! 🛫




