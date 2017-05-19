#!flask/bin/python
from flask import Flask, Markup, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/revision/<subject>')
@app.route('/revision/<subject>/<document>')
def normal(subject=None, document=None):
    content = subject,document

    return render_template('normal.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)