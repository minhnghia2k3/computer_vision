import os

import cv2
from PIL import Image

def load_image(path):
    """
    Read image from provided image path.
    :param path:
    :return: ImageFile
    """
    try:
        img = Image.open(path)
        return img
    except Exception as e:
        print("error while reading image ", path, " ", e)
        return None


def is_image_file(path):
    """
    Check if provided path is a valid image path.
    :param path:
    :return: bool
    """
    extensions = (".jpg", ".jpeg", ".png", ".gif")
    return path.lower().endswith(extensions)

def get_images_list(path):
    """
    Get images list from provided path.
    :param path:
    :return: ImageFile[]
    """

    image_list = []
    # check if path is existed and is directory
    if os.path.exists(path) and os.path.isdir(path):
        filenames = os.listdir(path)
        for filename in filenames:
            file_path = os.path.join(path, filename)
            if os.path.isfile(file_path) and is_image_file(file_path):
                img = load_image(file_path)
                image_list.append(img)
    return image_list

def display_img(title, img):
    cv2.imshow(title, img)
    cv2.waitKey(0)
    cv2.destroyWindow(title)