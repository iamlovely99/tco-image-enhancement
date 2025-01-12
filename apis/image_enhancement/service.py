import os
import subprocess
from dotenv import load_dotenv

load_dotenv()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in os.getenv("ALLOWED_EXTENSIONS").split(",")

def executeShellCommand(cmd):
    # Running a shell command and capturing its output
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout