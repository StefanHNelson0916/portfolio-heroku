from flask import Flask, render_template, send_file

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/aboutMe')
def aboutMe():
    return render_template('aboutMe.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/download')
def download_copy():
    return send_file('static/resume.pdf', attachment_filename='StefanHNelson-resume.pdf')

if __name__ == "__main__":
    app.run()