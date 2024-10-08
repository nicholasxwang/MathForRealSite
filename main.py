from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def main():
    # team is the loaded json from static/team.json
    with open('static/team.json') as f:
        team = json.load(f)

    # list of all images in static/gallery
    gallery = []
    for file in os.listdir('static/gallery'):
        gallery.append(file)

    return render_template('index.html', team = team, gallery = gallery)

@app.route('/about-us')
def about_us():
    return render_template('about.html')

@app.route('/enroll')
def enroll():
    return render_template('enroll.html')


@app.route('/get-involved')
def get_involved():
    return render_template('get-involved.html')


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
