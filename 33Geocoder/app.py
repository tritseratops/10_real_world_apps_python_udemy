from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/select_file")
def select_file():
    return render_template("index.html", btn="download.html")

@app.route("/my_send_file", methods=['POST'])
def my_send_file():
    if request.method=='POST':
        file = request.files['file']
        file.save(secure_filename(file.filename))
        with open(file.filename, "a") as f:
            f.write("This is added after upload.")
        return render_template("index.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email = request.form['email_name']
        height =  request.form['height_name']
        print(email + " " + height)
        data = Data(email, height)
        # print(db.session.query(Data).filter(Data.email_==email).count())
        return render_template("index.html", text = "Seems like we 've got something from this email address already")

@app.route("/download")
def download():
    return send_file("Sample.csv", attachment_filename="yourfile.csv", as_attachment=True)

if __name__ == '__main__':
    app.debug  = True
    app.run()