from flask import Response, request, jsonify, send_file
from flask_restful import Resource, reqparse
from werkzeug.utils import secure_filename
import os
from dotenv import load_dotenv
from PIL import Image
import uuid
# import shutil
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
            foldername = str(uuid.uuid4()).replace('-', '')[:20]
            file_extension = file.filename.rsplit('.', 1)[1].lower()
            filename = foldername+"."+file_extension
            folderpath = os.path.join(os.getenv("UPLOAD_PATH"), foldername, "input")
            output_folderpath = os.path.join(os.getenv("UPLOAD_PATH"), foldername, "output")
            os.makedirs(folderpath)
            os.makedirs(output_folderpath)
            # Save the file to the upload folder
            filepath = os.path.join(folderpath, filename)
            file.save(filepath)
            
            # Process the image (example: open and get dimensions)
            with Image.open(filepath) as img:
                width, height = img.size

            stdout = executeShellCommand(["python3", "run.py", "--input_folder", folderpath, "--output_folder", output_folderpath, "--GPU", "0"])
            print(stdout)
            output_filepath = os.path.join(output_folderpath, "final_output", filename)
            mimetype = "image/"+file_extension
            return send_file(output_filepath, mimetype)
            # return shutil.rmtree('/path/to/your/dir/')
            
            # return jsonify({
            #     'message': 'File processed successfully',
            #     'filename': filename,
            #     'width': width,
            #     'height': height
            # })
        else:
            return jsonify({'error': 'Invalid file type. Only JPEG and PNG images are allowed.'})
