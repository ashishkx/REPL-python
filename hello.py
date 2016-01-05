from flask import Flask, request, render_template
import os
app = Flask(__name__)


makefile(user_code):
	f = open("textarea_input.py", "w+")
	f.write(user_code)
	f.close()
		
@app.route('/', methods=['GET', 'POST'])
def index():
    new_text=""
    if request.method == 'POST':
        text = request.form['userinput']
        makefile(text)
		os.system("python textarea_input.py")
    return render_template('index.html', userout=)