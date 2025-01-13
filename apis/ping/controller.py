from flask import jsonify
from flask_restful import Resource

class Ping(Resource):
    
    def get(self):
        print("Ping OK.")
        return jsonify({'code': 200})
