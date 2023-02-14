from os import path

from werkzeug.utils import secure_filename

from app.config import config
from app.errors.image_processor_error import (
    InvalidImageProcessorRequestError,
    WrongImageFormatError,
)


class ImageProcessorService:
    def __init__(self, image_file=None):
        if not image_file:
            raise InvalidImageProcessorRequestError("File image not found")
        if not image_file.filename:
            raise InvalidImageProcessorRequestError("File image have no name")
        if not self.allowed_file(image_file.filename):
            raise WrongImageFormatError("Wrong image format")
        self.image_file = image_file
        self.image_file.filename = secure_filename(self.image_file.filename)
        self.image_file.save(path.join(config.UPLOAD_FOLDER, self.image_file.filename))

    @staticmethod
    def allowed_file(image_name):
        return (
            "." in image_name
            and image_name.rsplit(".", 1)[1].lower() in config.ALLOWED_EXTENSIONS
        )

    def remove_background(self):
        pass

    def get_coordinates_outlines_of(self):
        pass
