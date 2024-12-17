# Simulating a basic messaging system between two users

# Define user credentials (you can extend this for more users if needed)
users = {
    'user1': {'id': 'user1', 'password': 'password1', 'message': ''},
    'user2': {'id': 'user2', 'password': 'password2', 'message': ''}
}

# Function to login a user
def login(user_id, password):
    if user_id in users:
        if users[user_id]['password'] == password:
            print(f"Login successful for {user_id}!")
            return True
        else:
            print("Incorrect password.")
            return False
    else:
        print("User ID not found.")
        return False

# Function for one user to send a custom message to another user
def send_message(from_user, to_user, message):
    if from_user in users and to_user in users:
        users[to_user]['message'] = message
        print(f"{from_user} sent a message to {to_user}: {message}")
    else:
        print("Invalid user(s) specified.")

# Function for a user to check for new messages
def check_messages(user_id):
    if users[user_id]['message']:
        print(f"{user_id} received a message: {users[user_id]['message']}")
    else:
        print(f"No messages for {user_id}.")

# Main flow
def main():
    while True:
        # User1 login
        print("\nUser1, please log in:")
        user1_id = input("Username: ")
        user1_password = input("Enter password: ")

        if login(user1_id, user1_password):
            # User1 enters a custom message
            user1_message = input("Enter your message to send to user2: ")
            send_message('user1', 'user2', user1_message)

            # User2 login and check messages
            print("\nUser2, please log in:")
            user2_id = input("Username: ")
            user2_password = input("Enter password: ")

            if login(user2_id, user2_password):
                check_messages('user2')

                # Ask user2 if they want to send a message back to user1
                send_reply = input("Do you want to send a message to user1? (yes/no): ").strip().lower()

                if send_reply == 'yes':
                    # User2 enters a custom message
                    user2_message = input("Enter your message to send to user1: ")
                    send_message('user2', 'user1', user2_message)

                    # User1 checks the response
                    check_messages('user1')
                else:
                    print("No message sent to user1.")

        # Option to exit or continue
        cont = input("\nDo you want to continue? (yes/no): ").strip().lower()
        if cont != 'yes':
            break

if __name__ == "__main__":
    main()
