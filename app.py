from flask import Flask, jsonify, request
import random

app = Flask(__name__)

# A pool of fun DevOps/Linux troubleshooting scenarios
scenarios = [
    {
        "id": 1,
        "problem": (
            "The web server is down, and you suspect port 80 is already in use by another process. "
            "How do you check what is listening on port 80?"
        ),
        "accepted_commands": ["netstat", "ss", "lsof"]
    },
    {
        "id": 2,
        "problem": (
            "An application is running out of disk space because of a massive log file. "
            "You need to find files larger than 100MB in /var/log. What command do you use?"
        ),
        "accepted_commands": ["find"]
    },
    {
        "id": 3,
        "problem": (
            "A developer pushed code that broke the backend, and you need to see the container logs "
            "for a Docker container named 'api-server'. What do you type?"
        ),
        "accepted_commands": ["docker logs"]
    }
]


@app.route('/')
def home():
    return jsonify({
        "game": "DevOps Command Quiz API",
        "status": "ready",
        "hint": "Go to /api/quiz to get a challenge!"
    })


@app.route('/api/quiz', methods=['GET'])
def get_quiz():
    # Pick a random scenario but hide the answers from the payload
    quiz_item = random.choice(scenarios)
    return jsonify({
        "id": quiz_item["id"],
        "problem": quiz_item["problem"]
    })


@app.route('/api/quiz/submit', methods=['POST'])
def submit_answer():
    data = request.get_json() or {}
    scen_id = data.get("id")
    user_command = data.get("command", "").lower().strip()

    # Find the matching scenario
    scen = next((s for s in scenarios if s["id"] == scen_id), None)
    if not scen:
        return jsonify({"error": "Scenario not found"}), 404

    # Check if any accepted keyword is in the user's input command
    correct = any(keyword in user_command for keyword in scen["accepted_commands"])

    if correct:
        return jsonify({"correct": True, "message": "System restored! Excellent troubleshooting."})
    return jsonify({"correct": False, "message": "Command failed or didn't resolve the issue. Try again!"})

if __name__ == '__main__':
    import os
    # Render dynamic port pass karega, local par automatic 5000 use hoga
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)