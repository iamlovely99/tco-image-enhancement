from flask import Response, request, jsonify
from flask_restful import Resource, reqparse
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
from PIL import Image
import subprocess
from .service import allowed_file, executeShellCommand

load_dotenv()

class ImageEnhancement(Resource):
    
    def post(self):
        # body = request.get_json()
        # Check if a file was uploaded
        if 'image' not in request.files:
            return jsonify({'error': 'No file part'})
        
        file = request.files['image']
        
        # If no file is selected
        if file.filename == '':
            return jsonify({'error': 'No selected file'})
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            
            # Save the file to the upload folder
            filepath = os.path.join(os.getenv("UPLOAD_PATH"), filename)
            file.save(filepath)
            
            # Process the image (example: open and get dimensions)
            with Image.open(filepath) as img:
                width, height = img.size

            stdout = executeShellCommand(["python3", "run.py", "--input_folder", os.getenv("UPLOAD_PATH"), "--output_folder", os.getenv("OUTPUT_PATH"), "--GPU", "0"])
            print(stdout)
            
            return jsonify({
                'message': 'File processed successfully',
                'filename': filename,
                'width': width,
                'height': height
            })
        else:
            return jsonify({'error': 'Invalid file type. Only JPEG images are allowed.'})
