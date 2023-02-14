import os
from dataclasses import dataclass


# pylint: disable=invalid-name
@dataclass
class Config:
    FLASK_APP: str = os.environ.get("FLASK_APP")
    ENV: str = os.environ.get("ENV")
    UPLOAD_FOLDER: str = os.environ.get("UPLOAD_FOLDER")
    ALLOWED_EXTENSIONS: frozenset = frozenset(
        os.environ.get("ALLOWED_EXTENSIONS").split(",")
    )


config: Config = Config()
