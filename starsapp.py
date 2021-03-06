from flask import Flask,render_template
import urllib2
import json

app = Flask(__name__)

@app.route('/')
def root():

    u = urllib2.urlopen("https://api.nasa.gov/planetary/apod?api_key=uSmQ6NYPYM7iV8HcjWFCMvFE9RWul1QM65rTKKvl")
    d = json.loads(u.read())
    title = d['title']
    date = d['date']
    url = d['url']
    explanation = d['explanation']
    hdurl = d['hdurl']
    return render_template('base.html',title=title,date=date,url=url\
                           ,explanation=explanation,hdurl=hdurl)

@app.route('/tunes')
def tunes():

    u = urllib2.urlopen("https://itunes.apple.com/search?term=approaching+nirvana&entity=album&collectionExplicitness=notExplicit&limit=20")
    d = json.loads(u.read())
    print(d)
    print()
    return render_template('tunes.html',artist="Approaching Nirvana",list = d['results'])

if __name__ == '__main__':
    app.debug = True
    app.run()

