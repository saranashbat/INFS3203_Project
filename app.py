from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/SignUp', methods=['GET', 'POST'])  
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        email = request.form.get('email')
        fullname = request.form.get('fullname')
        # Process sign up data here
        return render_template('index.html')
    else:
        return render_template('signup.html')

@app.route('/infotechjobs')
def infoTechJobs():
    return render_template('infotechjobs.html')

@app.route('/infotechjob1')
def infoTechJob1():
    return render_template('infotechjob1.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
