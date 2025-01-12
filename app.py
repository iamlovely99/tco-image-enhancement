from flask import Flask
from flask_restful import Api
import os
from dotenv import load_dotenv
from apis.routes import initialize_routes

load_dotenv()

app = Flask(__name__)
api = Api(app)

initialize_routes(api)

app.run(debug=os.getenv("DEBUG"), host=os.getenv("HOST"), port=os.getenv("PORT"), threaded=True)