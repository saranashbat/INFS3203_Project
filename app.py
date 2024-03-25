from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') 


@app.route('/infotechjobs')
def infoTechJobs():
    return render_template('infotechjobs.html')

@app.route('/infotechjob1')
def infoTechJob1():
    return render_template('infotechjob1.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000) 