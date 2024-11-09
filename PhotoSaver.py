from os import path, mkdir
from PIL import Image
from io import BytesIO


SAVE_DIR_NAME = "ur_screens"
PHOTO_FORMAT = ".png"


# STATIC_CLASS!!!!!
class PhotoSaver:
    @staticmethod
    def save_photo(photo_data, photo_name):
        if not path.exists(SAVE_DIR_NAME):
            mkdir(SAVE_DIR_NAME)

        img = Image.open(BytesIO(photo_data.content))
        img.save(SAVE_DIR_NAME + '\\' + photo_name + PHOTO_FORMAT)
