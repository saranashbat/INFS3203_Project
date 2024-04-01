from flask import Flask, render_template, request, redirect
from flask_login import LoginManager, current_user, login_user, login_required

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Add a secret key for session security
login_manager = LoginManager(app)

# Mock user database
class User:
    def __init__(self, id, username, email, fullname):
        self.id = id
        self.username = username
        self.email = email
        self.fullname = fullname

users = {'example_user': User('1', 'example_user', 'example@example.com', 'Example User')}

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
        if user and password == 'example_password':  # Add your authentication logic here
            login_user(user)
            return redirect('/')
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
        # Process sign up data here
        # Example: Save the new user to the database
        return redirect('/')  # Redirect to the home page after successful sign up
    else:
        return render_template('SignUp.html')

@app.route('/profile')
@login_required
def profile():
    user_info = {
        'username': current_user.username,
        'email': current_user.email,
        'fullname': current_user.fullname
    }
    return render_template('profile.html', user_info=user_info)

@app.route('/infotechjobs')
def infoTechJobs():
    return render_template('infotechjobs.html')

@app.route('/infotechjob1')
def infoTechJob1():
    return render_template('infotechjob1.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
