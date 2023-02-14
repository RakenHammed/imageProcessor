from flask import Blueprint, request

from app.errors.image_processor_error import (
    InvalidImageProcessorRequestError,
    WrongImageFormatError,
)
from app.logger import logger
from app.services.image_processor_service import ImageProcessorService

bp = Blueprint("image_processor_controller", __name__, url_prefix="/imageProcessor")


@bp.route("/", methods=["POST"])
def process_image():
    image_file = request.files.get("image")
    try:
        image_processor_service = ImageProcessorService(image_file)
        response = {"result": image_processor_service.get_coordinates_outlines_of()}
        return response, 200
    except InvalidImageProcessorRequestError as error:
        logger.error(error)
        return str(error), 400
    except WrongImageFormatError as error:
        logger.error(error)
        return str(error), 400
