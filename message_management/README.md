Project Description: User Messaging System with Flask
Overview:
This project implements a simple user messaging system using Flask, a lightweight web framework for Python. The application allows users to log in with a username and password, send messages to other users, and view their own messages. It uses an in-memory database (a dictionary) to store user credentials and messages, and Flask’s session management to handle user authentication and session states.

Features:
User Authentication:
Users must log in with a username and password.
Passwords are securely stored using hashing (with werkzeug.security).
Upon successful login, users are directed to a dashboard page.
Dashboard:
Once logged in, users can select another user from a list and send messages to them.
Users can type a custom message and send it to the selected recipient.
The system ensures that users cannot send messages to themselves.
Message Viewing:
Users can view their own messages on a separate page.
Each user can see the messages that have been sent specifically to them, including the sender's name.
Logout:
Users can log out at any time, which will end their session and redirect them back to the login page.
Technology Stack:
Flask: Web framework used to handle routing, templates, and session management.
Werkzeug: For password hashing and checking (e.g., generate_password_hash and check_password_hash).
HTML/CSS: For the user interface.
In-Memory Database: A dictionary (users) to store usernames, passwords (hashed), and messages.
Flow of the Application:
Login Page:

The user enters their username and password.
If the credentials are correct, the user is redirected to the dashboard.
If the credentials are incorrect, an error message is displayed.
Dashboard Page:

After a successful login, the user is directed to the dashboard.
They can send messages to other users (excluding themselves).
A list of available users to message is presented in a dropdown menu.
Message Page:

Users can view all messages sent to them by other users.
If there are no messages, a message is displayed indicating the inbox is empty.
Logout:

The user can log out at any time, ending the session and redirecting to the login page.
Code Breakdown:
main.py: The core of the application, handling all routing, session management, and interactions with the in-memory user data.

Routes:
/: Home route, which checks if the user is logged in and redirects accordingly.
/login: Displays the login form and handles authentication.
/dashboard: Displays the dashboard with the option to send messages to other users.
/messages: Displays the messages that are sent to the logged-in user.
/logout: Logs the user out and clears the session.
HTML Templates:

login.html: The login page where users can enter their credentials.
dashboard.html: The dashboard where users can send messages and view other users.
messages.html: The page where users can view messages that have been sent to them.
Security Considerations:
Password Hashing: Passwords are not stored in plain text. Instead, they are hashed using werkzeug.security.generate_password_hash, ensuring that even if the in-memory database is exposed, passwords remain secure.

Session Management: Flask's session handling mechanism is used to track logged-in users. This helps prevent unauthorized access to the dashboard and messages pages.

Future Enhancements:
Persistent Database: Implementing a database (e.g., SQLite or PostgreSQL) to store user data and messages instead of using an in-memory dictionary, allowing data persistence across server restarts.
User Registration: Allow new users to register and create an account.
User Profiles: Add profile pages where users can view and update their personal information.
Message Deletion: Enable users to delete messages or conversations.
Admin Panel: Introduce an admin interface to manage users and monitor messages.
Use Case Example:
User1 logs in with the username user1 and password password1.
User1 goes to the dashboard, selects user2 from the user list, and sends a message: "Hello user2!".
User2 logs in and sees the message from user1 on their message page.
User2 can reply to user1 via the dashboard, sending "Hello user1! How are you?".
This simple messaging system can be extended to include more features such as notifications, real-time messaging, or group messaging, depending on the requirements.
