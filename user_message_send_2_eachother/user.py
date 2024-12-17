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

# Function for user1 to send a custom message to user2
def send_message(from_user, to_user, message):
    if from_user == 'user1' and to_user == 'user2':
        users['user2']['message'] = message
        print(f"{from_user} sent a message to {to_user}: {message}")
    else:
        print("Message can only be sent from user1 to user2.")

# Function for user2 to check for new messages
def check_messages(user_id):
    if user_id == 'user2' and users['user2']['message']:
        print(f"{user_id} received a message: {users['user2']['message']}")
    else:
        print(f"No messages for {user_id}.")

# Main flow
def main():
    # User1 login
    print("please enter your credentials:")
    user1_id = input("Username: ")
    user1_password = input("Enter password: ")

    if login(user1_id, user1_password):
        # User1 enters a custom message
        user1_message = input("Enter your message to send: ")
        send_message('user1', 'user2', user1_message)

        # User2 login and check messages
        print("\nUser, please log in:")
        user2_id = input("Username: ")
        user2_password = input("Enter password: ")

        if login(user2_id, user2_password):
            check_messages('user2')

if __name__ == "__main__":
    main()
