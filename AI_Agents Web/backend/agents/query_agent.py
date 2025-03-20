# backend/agents/query_agent.py
def get_academic_info(query):
    responses = {
        "backlog exam": "Next backlog exam is on 15th April.",
        "academic calendar": "The academic calendar is available at /calendar.pdf."
    }
    return responses.get(query.lower(), "I'm not sure. Please check with the admin.")
