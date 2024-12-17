from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Define user credentials and messages
users = {
    'user1': {'id': 'user1', 'password': 'password1', 'message': ''},
    'user2': {'id': 'user2', 'password': 'password2', 'message': ''}
}

# Function to login a user
def login(user_id, password):
    if user_id in users and users[user_id]['password'] == password:
        return True
    return False

# Route to login page
@app.route('/')
def home():
    return render_template('login.html')

# Route to handle login
@app.route('/login', methods=['POST'])
def login_user():
    user_id = request.form['username']
    password = request.form['password']
    
    if login(user_id, password):
        return redirect(url_for('dashboard', user_id=user_id))
    else:
        flash("Invalid login credentials")
        return redirect(url_for('home'))

# Route for user1's dashboard (where they can send a message to user2)
@app.route('/dashboard/<user_id>', methods=['GET', 'POST'])
def dashboard(user_id):
    if request.method == 'POST':
        message = request.form['message']
        if user_id == 'user1':
            users['user2']['message'] = message
            flash(f"Message sent to user2: {message}")
            return render_template('user1_dashboard.html', message=message)
        elif user_id == 'user2':
            reply = request.form['message']
            users['user1']['message'] = reply
            flash(f"Message sent to user1: {reply}")
            return render_template('user2_dashboard.html', reply=reply)
    else:
        if user_id == 'user1':
            return render_template('user1_dashboard.html')
        elif user_id == 'user2' and users['user2']['message']:
            return render_template('user2_dashboard.html', message=users['user2']['message'])
        else:
            return render_template('user2_dashboard.html')

if __name__ == '__main__':
    app.run(debug=True)
