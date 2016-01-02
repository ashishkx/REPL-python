from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello World!'
	
@app.route('/<user>')
def hello_world2(user):
	return 'Hello World %s! <h1 color = red> This is html right here </h1> %s' % (user, request.method)
		
@app.route('/index/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		text = request.form['userinput']
		new_text = ' You wrote this: %s' % text
		
	return render_template('index.html')
	
	

	

if __name__ == '__main__':
	app.run()
