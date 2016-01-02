from flask import Flask, request, render_template
app = Flask(__name__)

		
@app.route('/', methods=['GET', 'POST'])
def index():
    new_text=""
    if request.method == 'POST':
        text = request.form['userinput']
        new_text = '%s\n'%text + text.upper()

    return render_template('index.html', userout=new_text)

	
	

	

if __name__ == '__main__':
    app.run()
