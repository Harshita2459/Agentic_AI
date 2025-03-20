from flask import Flask, request, jsonify
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from backend.agents.leave_agent import process_leave_request
from backend.agents.certificate_agent import generate_certificate
from backend.agents.query_agent import get_academic_info

app = Flask(__name__)

@app.route("/apply_leave", methods=["POST"])
def apply_leave():
    data = request.json
    name = data.get("name", "User")  
    response = process_leave_request(data["employee_id"], data["leave_type"], data["start_date"], data["end_date"])
    return jsonify({
        "message": f"Applying leave for {name}...",
        "details": response
    })

@app.route("/generate_certificate", methods=["POST"])
def certificate():
    data = request.json
    name = data.get("name", "User")  
    response = generate_certificate(data["user_id"], data["certificate_type"])
    return jsonify({
        "message": f"Generating certificate for {name}...",
        "details": response
    })

@app.route('/academic_query', methods=['GET'])
def academic_query():
    query = request.args.get('query')

    if not query:
        return jsonify({"response": "Query is missing!"})

    responses = {
        "semester result": "Here is your semester result...SGPA: ...",
        "backlog exam": """To apply for the backlog exam, follow these steps:
        1. Visit the student portal and log in.
        2. Navigate to 'Examinations' > 'Backlog Exam Registration'.
        3. Select the subjects you want to reappear for.
        4. Pay the backlog exam fee online.
        5. Download the confirmation receipt.
        6. Admit cards will be available 7 days before the exam.
        The next backlog exam is scheduled for 15th April.""",
        "academic calendar": "The academic calendar is available at /calendar.pdf.",
        "exam schedule": "The exam schedule will be released next week.",
        "revaluation process": "Revaluation forms are available at the admin office. Last date to apply is 10th March.",
        "class timetable": "Your class timetable can be accessed through the student portal.",
        "attendance status": "You can check your attendance status in the student portal under 'Attendance'.",
        "library hours": "Library is open from 9 AM to 8 PM on weekdays and 10 AM to 5 PM on weekends.",
        "internship opportunities": "Check the internship portal for the latest opportunities.",
        "scholarship details": "Scholarship details are available at /scholarships.",
        "course registration": "Course registration starts from 1st April. Register via the student portal.",
        "fee payment deadline": "The last date for fee payment is 20th March.",
        "convocation details": "Convocation ceremony will be held on 30th June. More details at /convocation.",
    }

    response_text = responses.get(query.lower(), "I'm not sure. Please check with the admin.")
    
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
