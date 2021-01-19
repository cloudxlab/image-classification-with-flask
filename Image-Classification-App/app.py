# Flask utils
from flask import Flask, request, render_template
from werkzeug.utils import secure_filename
import os
from app_helper import *

# Define a flask app
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route('/uploader', methods = ['POST'])
def upload_file():
    predictions=""

    if request.method == 'POST':
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'static','uploads', secure_filename(f.filename))
        f.save(file_path)

        predictions = get_classes(file_path)
        pred_strings = []
        for _,pred_class,pred_prob in predictions:
            pred_strings.append(str(pred_class).strip()+" : "+str(round(pred_prob,5)).strip())
        preds = ", ".join(pred_strings)
        print("preds:::",preds)
    return render_template("upload.html", predictions=preds, display_image=f.filename) 


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True,port="4100")
