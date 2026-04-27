from enum import Enum

class Status(Enum):
    READY = "No image selected yet"
    IMAGE_SELECTED = "Image selected"

class ErrorStatus(Enum):
    NO_FILE = "Error: No file selected"
    NOT_IMAGE = "Error: Not an image file"