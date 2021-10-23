from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from sqlalchemy import func
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgressa@localhost/height_collector'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    height_ = db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_ = email_
        self.height_ = height_


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/select_file")
def select_file():
    return render_template("select_file.html", btn="download.html")

@app.route("/my_send_file", methods=['POST'])
def my_send_file():
    if request.method=='POST':
        file = request.files['file']
        file.save(secure_filename(file.filename))
        with open(file.filename, "a") as f:
            f.write("This is added after upload.")
        # content =  file.read()
        # print(content)
        # print(file)
        # print(type(file))

        return render_template("my_send_file.html")

@app.route("/success", methods=['POST'])
def success():
    if request.method=='POST':
        email = request.form['email_name']
        height =  request.form['height_name']
        print(email + " " + height)
        data = Data(email, height)
        # print(db.session.query(Data).filter(Data.email_==email).count())
        if (db.session.query(Data).filter(Data.email_==email).count()==0):
            print("NO SUCH KEY")
            db.session.add(data)
            db.session.commit()
            avg_height = db.session.query(func.avg(Data.height_)).scalar()
            avg_height = round(avg_height,1)
            heights_count = db.session.query(Data.height_).count()
            send_email(email, height, avg_height, heights_count)
            print("Count:"+str(heights_count))
            return render_template("success.html")
        return render_template("index.html", text = "Seems like we 've got something from this email address already")

@app.route("/download")
def download():
    # file = request.files["file"]
    return send_file("Sample.csv", attachment_filename="yourfile.csv", as_attachment=True)

if __name__ == '__main__':
    app.debug  = True
    app.run()