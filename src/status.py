from enum import Enum

class Status(Enum):
    READY = "Ready"
    IMAGE_SELECTED = "Image selected"

class ErrorStatus(Enum):
    NO_FILE = "No file selected"
    NOT_IMAGE = "Not an image file"