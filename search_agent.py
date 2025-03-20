from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

load_dotenv()

SimpleSearchAgent= Agent(
    name= "Web Agent",
    description= "This is the agent for searching content from the web",
    model= Groq(id= "llama-3.3-70b-versatile"),
    tools= [DuckDuckGo()],
    instructions="Always include the sources",
)
SimpleSearchAgent.print_response(
    message= "What is the capital of India?", stream=True
)