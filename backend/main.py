import binascii
import random
import os
import string
from flask import Flask, flash, request, redirect, url_for, send_from_directory
from flask_cors import CORS
from werkzeug.utils import secure_filename
from gtts import gTTS


UPLOAD_FOLDER = '/tmp'
TTS_FOLDER = 'tts'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['TTS_FOLDER'] = os.path.join(UPLOAD_FOLDER, TTS_FOLDER)

CORS(app)

NO_FILE_UPLOADED = 'NO FILE UPLOADED'

def gen_tts(txt):
    random_hash = binascii.hexlify(os.urandom(16)).decode('utf-8')
    filename = f"{random_hash}.mp3"
    tts = gTTS(text=txt, lang='pl')
    directory = app.config['TTS_FOLDER']
    if not os.path.exists(directory):
        os.makedirs(directory)
    tts.save(os.path.join(directory, filename))
    return filename


@app.route('/audio/<path:path>')
def serve_audio(path):
    return send_from_directory(app.config['TTS_FOLDER'], path)


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

        ### USE FILE FOR OCR

        # if not plain_text:
        #   plain_text OCR(UPLOAD_FOLDER + '/' + save_filename)

        ### USE FILE FOR AI

        # summary = AI(plain_text)
        # return summary

        return save_filename
