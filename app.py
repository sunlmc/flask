from flask import Flask,url_for
app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
@app.route('/user/<name>')
def user(name):
    return '<h1>Welcome to %s web page!</h1>' % name

@app.route('/test')
def test_url_for():
	print(url_for('user',name='lmc'))
	print(url_for('user',name='lly'))
	print(url_for('test_url_for'))
	print(url_for('test_url_for',num=2))
	return '<h2>Test page!</h2>'

