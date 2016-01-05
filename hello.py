from flask import Flask, request, render_template
import subprocess
app = Flask(__name__)


def makefile(user_code):
    f = open("textarea_input.py", "w+")
    f.write(user_code)
    f.close()
		
@app.route('/', methods=['GET', 'POST'])
def index():
    new_text=""
    if request.method == 'POST':
        text = request.form['userinput']
        makefile(text)
        proc = subprocess.Popen(["textarea_input.py"])
    return render_template('index.html', userout=None)
    
if __name__ == '__main__':
    app.run()