from flask import Flask, render_template, request, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# In-memory database for users and messages
users = {
    'user1': {'password': generate_password_hash('password1'), 'messages': []},
    'user2': {'password': generate_password_hash('password2'), 'messages': []},
    'user3': {'password': generate_password_hash('password3'), 'messages': []},
    'user4': {'password': generate_password_hash('password4'), 'messages': []},
    'user5': {'password': generate_password_hash('password5'), 'messages': []},
}

@app.route('/')
def home():
    if 'username' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and check_password_hash(users[username]['password'], password):
            session['username'] = username
            return redirect(url_for('dashboard'))
        else:
            return "Invalid credentials", 401
    return render_template('login.html')

@app.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    if 'username' not in session:
        return redirect(url_for('login'))

    username = session['username']
    if request.method == 'POST':
        recipient = request.form['recipient']
        message = request.form['message']
        
        if recipient in users and recipient != username:
            users[recipient]['messages'].append(f"Message from {username}: {message}")
            return redirect(url_for('dashboard'))

    return render_template('dashboard.html', username=username, users=users.keys())

@app.route('/messages')
def messages():
    if 'username' not in session:
        return redirect(url_for('login'))
    
    username = session['username']
    user_messages = users[username]['messages']
    
    return render_template('messages.html', username=username, messages=user_messages)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
