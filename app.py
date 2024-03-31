from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required

app = Flask(__name__)
app.secret_key = '1234' 

login_manager = LoginManager()
login_manager.init_app(app)

# Mock user database
class User(UserMixin):
    def __init__(self, id):
        self.id = id

users = {'user_id': User('user_id')}  # Replace 'user_id' with your actual user ID

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Mock authentication - Replace with your actual authentication logic
        if username == 'user' and password == 'password':
            user = User(username)
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/SignUp', methods=['GET', 'POST'])  
def SignUp():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        fullname = request.form['fullname']
        # Process sign up data here
        return render_template('index.html')
    else:
        return render_template('SignUp.html')

@app.route('/infotechjobs')
@login_required
def infoTechJobs():
    return render_template('infotechjobs.html')

@app.route('/infotechjob1')
@login_required
def infoTechJob1():
    return render_template('infotechjob1.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
