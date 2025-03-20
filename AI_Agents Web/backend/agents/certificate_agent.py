# backend/agents/certificate_agent.py
import json

def generate_certificate(user_id, cert_type):
    response = {
        "user_id": user_id,
        "certificate_type": cert_type,
        "status": "Generated",
        "download_link": f"/certificates/{user_id}_{cert_type}.pdf"
    }
    return json.dumps(response)
