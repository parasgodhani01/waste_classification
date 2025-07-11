# main.py
from flask import Flask, render_template, request, redirect, send_from_directory
from werkzeug.utils import secure_filename
import os
from model import predict

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        file = request.files['file']
        if file.filename == '':
            return render_template('index.html', error="No file selected")

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)  #type:ignore
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(filepath)
            file.stream.flush()
            file.close()

            try:
                label, confidence = predict(filepath)
            except Exception as e:
                return render_template('index.html', error=f"Prediction failed: {str(e)}")

            return render_template('index.html', result={
                'label': label,
                'confidence': round(confidence * 100, 2),
                'filename': filename,
                'image_url': f'/uploads/{filename}'
            })

        else:
            return render_template('index.html', error="Invalid file type. Please upload a PNG ,JPG or JPEG.")

    return render_template('index.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    app.run(debug=True)
