from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import os
from subprocess import check_output
from FloorplanToBlender3d import arun

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def convert_to_3d(input_path):
    a=arun.abc()

    # Your code for converting 2D blueprint to 3D model goes here
    # Replace this dummy function with your actual implementation
    return a

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        output_path = convert_to_3d(filepath)
        return send_file(output_path, as_attachment=True)
    return 'Invalid file'

if __name__ == '__main__':
    app.run(debug=True)
