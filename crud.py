# import sqlite3

# # Function to connect to SQLite database and create a table for Slack users
# def connect_to_database():
#     conn = sqlite3.connect('slack_usersdetails1.db')
#     cursor = conn.cursor()

#     # Create the table if it doesn't exist
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS slack_usersdetails2 (
#             id TEXT PRIMARY KEY,
#             name TEXT,
#             birthday DATE
#         )
#     ''')

#     return conn, cursor

# # Function to insert a new user into the slack_usersdetails table
# def insert_user(conn, cursor, user_id, user_name, user_birthday):
#     try:
#         cursor.execute('INSERT INTO slack_usersdetails1 (id, name, birthday) VALUES (?, ?, ?)', (user_id, user_name, user_birthday))
#         conn.commit()
#         print(f"User {user_name} ({user_id}) added successfully.")
#     except sqlite3.Error as e:
#         print(f"Error inserting user: {e}")
#         conn.rollback()

# def read_employees():
#     cursor.execute('SELECT * FROM slack_usersdetails1')
#     return cursor.fetchall()

# if __name__ == "__main__":
#     # Connect to the SQLite database
#     conn, cursor = connect_to_database()


#     # Insert a new user (example)
#     user_id = "U05SCUHNQRX"  # Replace with the actual user ID
#     user_name = "sasichithra98"  # Replace with the actual user name
#     user_birthday = "09-21"  # Replace with the actual birthday in "MM-DD" format

#     # insert_user(conn, cursor, user_id, user_name, user_birthday)

#     # user_id = "U05"  # Replace with the actual user ID
#     # user_name = "sasi"  # Replace with the actual user name
#     # user_birthday = "09-20"  # Replace with the actual birthday in "MM-DD" format

#     insert_user(conn, cursor, user_id, user_name, user_birthday)

#     print(read_employees())

#     # Close the database connection
#     conn.close()
import sqlite3

# Function to connect to SQLite database and create a table for Slack users
def connect_to_database():
    conn = sqlite3.connect('slack_usersdetails1.db')
    cursor = conn.cursor()

    # Create the table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS slack_usersdetails1 (
            id TEXT PRIMARY KEY,
            name TEXT,
            birthday DATE
        )
    ''')

    return conn, cursor

# Function to insert a new user into the slack_usersdetails1 table
def insert_user(conn, cursor, user_id, user_name, user_birthday):
    try:
        cursor.execute('INSERT INTO slack_usersdetails1 (id, name, birthday) VALUES (?, ?, ?)', (user_id, user_name, user_birthday))
        conn.commit()
        print(f"User {user_name} ({user_id}) added successfully.")
    except sqlite3.Error as e:
        print(f"Error inserting user: {e}")
        conn.rollback()

# Function to update the birthday of a user in the slack_usersdetails1 table
def update_user_birthday(conn, cursor, user_id, new_birthday):
    try:
        cursor.execute('UPDATE slack_usersdetails1 SET birthday = ? WHERE id = ?', (new_birthday, user_id))
        conn.commit()
        print(f"Birthday updated successfully for user {user_id}.")
    except sqlite3.Error as e:
        print(f"Error updating birthday: {e}")
        conn.rollback()

def read_employees():
    cursor.execute('SELECT * FROM slack_usersdetails1')
    return cursor.fetchall()

if __name__ == "__main__":
    # Connect to the SQLite database
    conn, cursor = connect_to_database()

    # Insert a new user (example)
    user_id = "U05SCUHNQRX"  # Replace with the actual user ID
    user_name = "sasichithra98"  # Replace with the actual user name
    user_birthday = "09-21"  # Replace with the actual birthday in "MM-DD" format

    # insert_user(conn, cursor, user_id, user_name, user_birthday)

    # Update the birthday for a user (example)
    user_id_to_update = "U05SCUHNQRX"  # Replace with the actual user ID to update
    new_birthday = "09-26"  # Replace with the new birthday in "MM-DD" format

    update_user_birthday(conn, cursor, user_id_to_update, new_birthday)

    print(read_employees())

    # Close the database connection
    conn.close()
