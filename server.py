#! /usr/bin/env python3
import cv2
import os
from flask import Flask, request, redirect, url_for, send_from_directory
from werkzeug.utils import secure_filename
#import cvDetector
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

classNames = {1: 'CB'}

def id_class_name(class_id, classes):
    for key, value in classes.items():
        if class_id == key:
            return value

def cvDetector(filename):
    # Loading model
    model = cv2.dnn.readNetFromTensorflow('model_TF/frozen_inference_graph.pb',
                                        'model_TF/5OCVgraph.pbtxt')
    image = cv2.imread(filename)

    image_height, image_width, _ = image.shape

    model.setInput(cv2.dnn.blobFromImage(image, size=(300, 300), swapRB=True))
    output = model.forward()
    # print(output[0,0,:,:].shape)
    X = 0
    #Y = 0
    #Z = 0

    for detection in output[0, 0, :, :]:
        confidence = detection[2]
        if confidence > .3:
            class_id = detection[1]
            if class_id == 1.0 :
                X = X + 1
    return X

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
  # this has changed from the original example because the original did not work for me
    return filename[-3:].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            print '**found file', file.filename
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #for browser, add 'redirect' function on top of 'url_for'
            print type(file.filename)
            print cvDetector(file.filename)
            return url_for('uploaded_file',
                                    filename=filename)
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename)

if __name__ == '__main__':
    app.run(debug=True)
