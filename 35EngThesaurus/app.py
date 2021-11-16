from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import json
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/show_meaning", methods=['POST'])
def show_meaning():
    print('Inside show meaning file')
    if request.method=='POST':
        input_text = request.POST.get('input_text')
        print("input_text:"+input_text)
        description = ""
        return render_template('index.html', output_text=description)


if __name__ == '__main__':
    app.debug  = True
    app.run()