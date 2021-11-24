from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
from dashboard import create_chart

app = Flask(__name__)

@app.route("/")
def index():
    script_source, div_source, cdn_js = create_chart()
    return render_template("index.html", script_source = script_source, div_source = div_source, cdn_js = cdn_js)

if __name__ == '__main__':
    app.debug  = True
    app.run()