from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv
import os

load_dotenv()

agent=Agent(
    model= Groq(
        id= "mixtral-8x7b-32768",
    ),
    tools= [DuckDuckGo()],
    instructions="Always provide detailed analysis and include sources for information",
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

def analyze_image_and_search(image_url :str, query:str):

    try:
        messages=[
            {"role":"system", "content":"You are an AI agent. Please analyze images and provide detailed responses."},
            {"role":"user", "content":f"Analyze the image at this URL: {image_url} and answer the query: {query}"}
        ]

        response=agent.run(messages=messages, stream=True)
        for chunk in response:
            print (chunk)

    except Exception as e:
        print(f"Error processing Image: {str(e)}")

if __name__== "__main__":
    image_url="https://en.wikipedia.org/wiki/Kalinga_Institute_of_Industrial_Technology#/media/File:Kiit_library_building.jpg"
    query= "Tell me about the location and purpose of the building. Include any recnt news or developments."

    analyze_image_and_search(image_url, query)