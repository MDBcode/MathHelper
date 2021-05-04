from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
import os
import main

app = Flask(__name__)
Bootstrap(app)

path = os.getcwd()
UPLOAD_FOLDER = os.path.join(path, 'static/images')
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/", methods=["POST", "GET"])
def upload_file():
    uploaded_file = request.files['file']
    if uploaded_file.filename != '':
        uploaded_file.save(os.path.join(
            app.config["UPLOAD_FOLDER"], uploaded_file.filename))
        result = main.boss(uploaded_file.filename)
        return render_template('results.html', data=result)
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0')
