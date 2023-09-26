import os
import sqlite3
import datetime
from slack import WebClient
from slack.errors import SlackApiError

# Initialize the Slack API client with your Slack bot token
slack_token = os.environ["SLACK_API_TOKEN"]
client = WebClient(token=slack_token)
print(f"slack_token: {slack_token}")


# Function to send a message to a Slack user
def send_slack_message(user, message):
    try:
         response = client.chat_postMessage(channel= user, text=message)
         print(f"Message sent to user {user}: {message}")
         return response["ok"]         
    except SlackApiError as e:
        print(f"Error sending message: {e.response['error']}")
    
def connect_to_database():
    conn = sqlite3.connect('slack_usersdetails1.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS slack_usersdetails1(
            id TEXT PRIMARY KEY,
            name TEXT,
            birthday DATE
        )
    ''')

    return conn, cursor
def get_today_date():
    return datetime.date.today().strftime("%m-%d")
def send_birthday_wishes(cursor):
    today = get_today_date()
    try:
        cursor.execute("SELECT id, birthday FROM slack_usersdetails1 WHERE birthday = ?", (today,))
        birthdays = cursor.fetchall()
        print(f"birthday : {birthdays}")
    except sqlite3.Error as e:
        print(f"SQlite error: {e}")

    for user_id, birthday in birthdays:
        message = f"Happy Birthday, <@{user_id}>! 🎉🎂"
        print(f"Sending message to user {user_id}: {message}")
        result = send_slack_message(user_id, message)
if __name__ == "__main__":
    # Connect to the SQLite database and fetch Slack user data
    conn, cursor = connect_to_database()
    # Send birthday wish 
    send_birthday_wishes(cursor)
    # Close the database connection 
    conn.close()