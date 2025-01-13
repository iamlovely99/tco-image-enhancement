from .ping.controller import Ping
from .image_enhancement.controller import ImageEnhancement

def initialize_routes(api):
    api.add_resource(Ping, '/ping')
    api.add_resource(ImageEnhancement, '/api/image-enhancement')