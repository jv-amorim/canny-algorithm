import cv2


class ImageUtils:

  def convert_bgr_img_to_grayscale(bgr_image):
    return cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)
