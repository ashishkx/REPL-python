from flask import Flask, request, render_template
import subprocess
app = Flask(__name__)


def makefile(user_code):
    f = open("textarea_input.py", "w+")
    f.write(user_code)
    f.close()
		
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['userinput']
        makefile(text)
        proc = subprocess.check_output(["python", "textarea_input.py"])
    return render_template('index.html', userout= proc)
    
if __name__ == '__main__':
    app.run()