from flask import Flask, render_template, request, redirect, session
from flask_login import LoginManager, current_user, login_user, login_required, logout_user
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for session security
login_manager = LoginManager(app)

# File to store user data
USERS_FILE = 'users.json'

# Mock user database
class User:
    def __init__(self, id, username, email, fullname, password):
        self.id = id
        self.username = username
        self.email = email
        self.fullname = fullname
        self.password = password
    
    def is_active(self):
        # For simplicity, assuming all users are active.
        return True
    
    def get_id(self):
        return str(self.id)
    
    def to_dict(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'fullname': self.fullname,
            'password': self.password
        }

# Save users to the JSON file
def save_users(users):
    users_dict = {username: user.to_dict() for username, user in users.items()}
    with open(USERS_FILE, 'w') as file:
        json.dump(users_dict, file)

# Load existing users from the JSON file
def load_users():
    try:
        with open(USERS_FILE, 'r') as file:
            users_dict = json.load(file)
            return {username: User(**user_data) for username, user_data in users_dict.items()}
    except FileNotFoundError:
        return {}

users = load_users()

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = users.get(username)
        if user:
            actualPass = user.password
            
            if password == actualPass: 
                login_user(user)
                session['username'] = user.username
                return redirect('/')
            else:
                return render_template('login.html', error='Invalid username or password')
        else:
            return render_template('login.html', error='Invalid username or password')

    else:
        return render_template('login.html')


@app.route('/SignUp', methods=['GET', 'POST'])
def SignUp():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        
        # Check if the username already exists
        if username in users:
            return render_template('SignUp.html', error='Username already exists')

        # Create a new user
        user_id = str(len(users) + 1)  # Generate a new user ID
        new_user = User(user_id, username, email, fullname, password)
        
        # Add the new user to the database
        users[username] = new_user
        
        # Save users to the JSON file
        save_users(users)
        
        return redirect('/')  # Redirect to the home page after successful sign up
    else:
        return render_template('SignUp.html')
    

@app.route('/logout')
def logout():
    if 'username' in session:
        session.clear()
    return redirect('/')

@app.route('/infotechjobs')
def infoTechJobs():
    return render_template('infotechjobs.html')

@app.route('/infotechjob1')
def infoTechJob1():
    return render_template('infotechjob1.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
