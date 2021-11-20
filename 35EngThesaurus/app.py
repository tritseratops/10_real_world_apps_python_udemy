from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from thesaurus import get_description

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/show_meaning", methods=['POST'])
def show_meaning():
    if request.method=='POST':
        input_text = request.form['input_text']
        print("input_text:"+input_text)
        description = get_description(input_text)
        return render_template('index.html', input_text=input_text, output_text=description)


if __name__ == '__main__':
    app.debug  = True
    app.run()