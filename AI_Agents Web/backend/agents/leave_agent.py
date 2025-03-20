# backend/agents/leave_agent.py
import json

def process_leave_request(employee_id, leave_type, start_date, end_date):
    # Placeholder logic for leave processing
    response = {
        "employee_id": employee_id,
        "leave_type": leave_type,
        "start_date": start_date,
        "end_date": end_date,
        "status": "Approved"  # Mock response
    }
    return json.dumps(response)
