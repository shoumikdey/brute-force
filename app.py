from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
from mobileNet import get_prediction
import os

app = Flask(__name__)

UPLOAD_FOLDER = ''
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['GET', 'POST'])
def img_upload():
    if request.method == 'POST':
        file = request.files['file']
        # print(file.filename)
        filename = secure_filename(file.filename)
        # print(filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        prediction = get_prediction(filename)
        os.remove(filename)
    return prediction[0][1]


if __name__ == '__main__':
    app.run(debug=True)
