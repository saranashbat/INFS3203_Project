from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = ''

login_manager = LoginManager()
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id, email, fullname):
        self.id = id
        self.email = email
        self.fullname = fullname

users = {'user': User('user', 'user@user.com', 'user')}  

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
        if username in users and password == 'password':
            user = users[username]
            login_user(user)
            return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        # Update user profile here
        current_user.email = request.form['new_email']
        current_user.fullname = request.form['new_fullname']
        return redirect(url_for('profile'))
    user_info = {
        'username': current_user.id, 
        'email': current_user.email,  
        'fullname': current_user.fullname         
    }
    return render_template('profile.html', user_info=user_info)

@app.route('/SignUp', methods=['GET', 'POST'])  
def SignUp():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        fullname = request.form['fullname']
        # Process sign up data here
        return redirect(url_for('home'))
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
