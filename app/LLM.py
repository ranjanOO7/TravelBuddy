from crewai import LLM
from dotenv import load_dotenv

load_dotenv()

def get_llm() -> LLM:
    return LLM(
        model="groq/llama-3.3-70b-versatile",
        temperature=0.3
    )