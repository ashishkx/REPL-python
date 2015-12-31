from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'
	
@app.route('/<user>')
def hello_world2(user):
	return 'Hello World %s! <h1 color = red> This is html right here </h1> %s' % (user, request.method)
	
@app.route('/index/')
def index():
	return render_template('index.html')

@app.route('/index/', methods=['POST'])
def index_post():
	text = request.form['textarea']
	new_text = ' You wrote this: %s' % text
	return new_text
	

if __name__ == '__main__':
	app.run()