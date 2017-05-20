#!flask/bin/python
from flask import abort, Flask, Markup, render_template
import json

revisionSubjects = ["cs", "geography", "maths"]

revisionPages = {"cs": ["abc","cba"], "geography": [],"maths": []}

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html',e=e), 404

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/work/')
@app.route('/work/<project>')
def work(project=None):
    if(project):
        title = "this project"
        content = "this project"
        return render_template("normal-htmlSafe.html", **locals())
    else:
        title = "All projects"
        content = "showing all projects"
        return render_template("normal-htmlSafe.html", **locals())

@app.route('/revision/')
@app.route('/revision/<subject>/')
@app.route('/revision/<subject>/<document>')
def revision(subject=None, document=None):
    if(subject):
        if(subject.lower() in revisionSubjects):

            if(document):
                title = document + " - " + subject + " | Jon Morgan"
                #load from file and present as markdown
                return render_template('revision-markdown.html', **locals())
            else:
                title = subject + " | Jon Morgan"
                content = subject,document # make heading then brief description
                subs = revisionPages[subject]

                return render_template('listing-index.html', **locals())
        else:
            abort(404)
    else:
        title = "Revision | Jon Morgan"
        subs = revisionSubjects
        return render_template('listing-index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)