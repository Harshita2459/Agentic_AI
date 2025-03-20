from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

finance_agent=Agent(
description= "your task is to find finance information",
model= Groq(id="llama-3.3-70b-versatile"),
tools=[
    YFinanceTools(
        stock_price=True,
        analyst_recommendations=True,
        company_info=True,
        company_news=True
    )
],
instructions=["Use tables to display data"],
show_tool_calls= True,
markdown= True,
debug_mode=True
)

finance_agent.print_response(
    "Summarize analyst recommendations for TSLA", stream=True
)