from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the code generation agent
code_agent = Agent(
    name="Code Generator",
    description="Generates basic Python code for user-defined tasks",
    model=Groq(id="llama-3.3-70b-versatile"),
    instructions="Generate Python code for the given task. Always ensure the code is syntactically correct and includes comments for clarity.",
    show_tool_calls=True,
    markdown=True,
    debug_mode=True
)

def generate_code(task_description):
    """
    Generate Python code for the given task description.

    Args:
        task_description (str): A description of the task for which code is to be generated.

    Returns:
        str: The generated Python code.
    """
    query = f"Write Python code to {task_description}. Include comments and make it beginner-friendly."
    response = code_agent.print_response(query, stream=True)
    return response

if __name__ == "__main__":
    while True:
        print("Enter a task description or type 'exit' to quit:")
        task = input("Task: ")
        if task.lower() == 'exit':
            print("Goodbye!")
            break
        try:
            print("\nGenerating code...\n")
            code = generate_code(task)
            print("\nGenerated Code:\n")
            print(code)
        except Exception as e:
            print(f"An error occurred: {str(e)}")
