#!flask/bin/python
import markdown
from flask import abort, Flask, Markup, render_template, request
import json, os

def createRevisionPages():
    f = os.listdir("static/revision")
    out = {}
    for subject in f:
        out.update({subject: {}})
        files = os.listdir("static/revision/"+subject)
        for file in files:
            if(file != "assets"):
                title, type = os.path.splitext("static/revision/" + subject +"/"+ file)
                title = title[len("static/revision/" + subject +"/"):]
                route = "/revision/"+subject+"/"+title
                out[subject].update({title:{"title": title, "type": type, "route":route}})
    return out

revisionSubjects = {"cs":{"route": "/revision/cs/",
                          "title":"Computer Science",
                          "description":"Revision notes for AQA A-Level Computer Science"
                          },
                    "geography": {"route": "/revision/geography/",
                                  "title": "Geography",
                                  "description":"Revision notes for AQA A-Level Geography (2030)"
                                  },
                    "maths": {"route": "/revision/maths/",
                              "title":"Maths",
                              "description":"Revision resources for Edexcel A-Level Maths"
                              }
                    }
revisionPages = createRevisionPages()

app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    url = request.url
    return render_template('404.html',e=e, url=url), 404

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
        content = '<div id="placeholderBox">Coming soon...</div>'
        return render_template("normal-htmlSafe.html", **locals())

@app.route('/revision/')
@app.route('/revision/<subject>/')
@app.route('/revision/<subject>/<document>')
def revision(subject=None, document=None):
    if(subject):
        topLevel = False
        if(subject.lower() in list(revisionSubjects.keys())):
            if(document):
                if(document.lower() in revisionPages[subject.lower()].keys()):
                    title = document + " - " + subject + " | Jon Morgan"
                    if(revisionPages[subject][document]["type"] == ".md"):
                        #load from file and present as markdown
                        content = Markup(markdown.markdown(open("static" + revisionPages[subject][document]["route"]+revisionPages[subject][document]["type"]).read()))
                        return render_template('normal.html', **locals())
                    else:
                        content = open("static"+revisionPages[subject][document]["route"]+revisionPages[subject][document]["type"]).read()
                        return render_template('normal-htmlSafe.html', **locals())
                else:
                    abort(404)
            else:
                title = subject + " | Jon Morgan"
                pageTitle = revisionSubjects[subject]["title"] + " Revision"

                content = revisionSubjects[subject]["description"]
                subs = revisionPages[subject]

                return render_template('listing-index.html', **locals())
        else:
            abort(404)
    else:
        title = "Revision | Jon Morgan"
        topLevel = True
        pageTitle = "Revision"
        content = ""
        subs = [revisionSubjects[x] for x in list(revisionSubjects.keys())]
        for i in range(len(subs)):

            subs[i].update({"pages": revisionPages[list(revisionSubjects.keys())[i]]})
            #print(subs[i])
        #print(subs)
        return render_template('listing-index.html', **locals())

if __name__ == '__main__':
    #app.run(debug=True)
    app.run(host='0.0.0.0', port=80)