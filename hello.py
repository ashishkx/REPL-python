from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    eval_text=None
    if request.method == 'POST':
        text = request.form['userinput']
        code_text = compile(text,'<string>','eval')
        eval_text = eval(code_text)
    return render_template('index.html', userout=eval_text)

if __name__ == '__main__':
    app.run(debug=True)
