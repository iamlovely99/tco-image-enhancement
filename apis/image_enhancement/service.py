import os
import subprocess
from dotenv import load_dotenv
from run_all.runModules import runAll

load_dotenv()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in os.getenv("ALLOWED_EXTENSIONS").split(",")

def executeShellCommand(cmd):
    # Running a shell command and capturing its output
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout

def runModules(params: dict):
    # Running a shell command and capturing its output
    result = runAll(params)
    return result