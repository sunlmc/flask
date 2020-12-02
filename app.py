from flask import Flask,url_for,render_template
app = Flask(__name__)

#initinal data
name = 'Lmc'
movies = [
	{'title': 'My Neighbor Totoro','year':'1988'},
	{'title': 'Dead Poets society','year':'1989'},
	{'title': 'A Perfect World','year':'1993'},
	{'title': 'Leon','year':'1994'},
	{'title': 'Mahjong','year':'1996'},
	{'title': 'The Pork of Music','year':'2012'}	
]

@app.route('/')
def index():
    return render_template('index.html',name=name,movies=movies)


