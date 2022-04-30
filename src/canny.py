from consts import GAUSSIAN_KERNEL_5
from kernel import apply_kernel_to_matrix


def apply_canny_edge_detector_to_img(img):
  canny_edge_detector = CannyEdgeDetector()
  canny_edge_detector.set_input_img(img)
  canny_edge_detector.apply_edge_detector()
  return canny_edge_detector.get_result_img()


class CannyEdgeDetector:

  def __init__(self):
    self.img = None
    self.result_img = None


  def set_input_img(self, img):
    if len(img.shape) != 2:
      raise ValueError('The input image must have only two dimensions!')

    self.img = img
    self.img_height, self.img_width = img.shape


  def apply_edge_detector(self):
    if self.img is None:
      raise ValueError('The input image must be setted before calling this method.')

    self.__smooth_the_img()

  def __smooth_the_img(self):
    self.result_img = apply_kernel_to_matrix(GAUSSIAN_KERNEL_5, self.img)


  def get_result_img(self):
    if self.result_img is None:
      raise ValueError('No result image have been found. Call the apply_edge_detector method before.')

    return self.result_img
