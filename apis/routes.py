from .image_enhancement.controller import ImageEnhancement

def initialize_routes(api):
    api.add_resource(ImageEnhancement, '/api/image-enhancement')