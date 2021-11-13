from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
# from pandas import DataFrame, read_csv
import pandas
from addgeocodes import add_geocodes
import datetime

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/show_table", methods=['POST'])
def show_table():
    print('Inside my send file')
    if request.method=='POST':
        file = request.files['file']
        print("filename:"+file.filename)
        try:
            df = pandas.read_csv(file)
            if 'Address' in df.columns or 'address' in df.columns:
                geo_df = add_geocodes(df)
                geo_filename = datetime.datetime.now().strftime("uploads/"+file.filename+"Y%-m%-d%-H%-M%-S%-f%"+".csv")
                geo_df.to_csv(secure_filename(geo_filename), sep=',')
                no_address_message= ""
                geo_df.to_html(header="true", table_id="table")
                return render_template('index.html', tables=[geo_df.to_html(classes='data')], titles=geo_df.columns.values, filename=geo_filename)
            else:
                # print that no address column found
                no_address_message = "Seems like three is no address column in this file"
                # text = "Seems like three is no address column in this file"
                return render_template('index.html', text=no_address_message)
        except:
            no_address_message = "Seems like this file cant be parsed"
            # text = "Seems like three is no address column in this file"
            return render_template('index.html', text=no_address_message)


@app.route("/download")
def download():
    return send_file("test.csv", attachment_filename="test.csv", as_attachment=True)

if __name__ == '__main__':
    app.debug  = True
    app.run()