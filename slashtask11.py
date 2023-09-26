import datetime
import os
from pathlib import Path
import sqlite3
from dotenv import load_dotenv
import requests
from flask import Flask, request, jsonify
from slack_bolt import App
from slack_bolt.adapter.flask import SlackRequestHandler
from slack_sdk import WebClient
app = Flask(__name__)
slack_app = App(
    token="xoxb-5884234002883-5884844160338-euBjyFVxPUFrMgcPapq3a4KC",
    signing_secret="78ab52e5e522338a722a4cce2ec1f120"
)


@app.route("/slack/command", methods=["POST"])
def command():
    # Parse request body data
    data = request.form

    # Call the appropriate function based on the slash command
    if data["command"] == "/joke":
        message = get_joke()
    elif data["command"] == "/list_users":
        message = list_users()
    else:
        print("yes")
        message = f"Noo Invalid command: {data['command']}"

    # Return response to Slack
    return jsonify({"text": message})
def get_joke():
    url = "https://icanhazdadjoke.com/"
    headers = {"Accept": "application/json"}
    response = requests.get(url, headers=headers, timeout=5)
    joke = response.json()["joke"]
    return joke
#get today date funtion
def get_today_date():
    return datetime.date.today().strftime("%m-%d")
#functions for list user
def list_users():
    conn = sqlite3.connect('slack_usersdetails1.db')
    cursor = conn.cursor()
    today = get_today_date()
    cursor.execute("SELECT id, name FROM slack_usersdetails1 WHERE birthday = ?", (today,))
    birthday_users = cursor.fetchall()
    for user_id, user_name in birthday_users:
        message = f"Today's Birthday, <@{user_id}>! 🎉🎂"
        return message


handler = SlackRequestHandler(slack_app)
if __name__ == "__main__":
    # Start the Flask app on port 5000
    app.run(port=5000, debug=True)