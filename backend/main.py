import binascii
import random
import textract
import text_processing
import os
from flask import Flask, flash, request, redirect, url_for, jsonify
from flask_cors import CORS
from werkzeug.utils import secure_filename


UPLOAD_FOLDER = '/tmp'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

CORS(app)

NO_FILE_UPLOADED = 'NO FILE UPLOADED'

@app.route('/', methods=['POST'])
def index():
    # check if the post request has the file part
    if 'file' not in request.files:
        return NO_FILE_UPLOADED, 400

    uploaded_file = request.files['file']

    # if user does not select file, browser also
    # submit an empty part without filename
    if uploaded_file.filename == '':
        return NO_FILE_UPLOADED, 400


    if uploaded_file:
        filename_full = secure_filename(uploaded_file.filename)
        extension = filename_full.rsplit('.', 1)[1]
        filename = filename_full.rsplit('.', 1)[0]
        save_filename = f"{filename}.{extension}"
        while os.path.exists(UPLOAD_FOLDER + '/' + save_filename):
            random_hash = binascii.hexlify(os.urandom(16)).decode('utf-8')
            save_filename = f"{filename}.{random_hash}.{extension}"
        uploaded_file.save(os.path.join(app.config['UPLOAD_FOLDER'], save_filename))

        text = textract.process(UPLOAD_FOLDER + '/' + save_filename, language="pol")

        analysis = text_processing.analysis(text.decode('utf-8'))

        return jsonify(analysis)
