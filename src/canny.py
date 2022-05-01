import numpy as np
from consts import GAUSSIAN_KERNEL_5, SOBEL_KERNEL_X, SOBEL_KERNEL_Y
from kernel import apply_kernel_to_matrix
from math import pi


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

    self.result_img = np.zeros(self.img.shape)

    self.__smooth_with_gaussian_kernel()
    self.__calculate_gradient_with_sobel_kernels()
    self.__calculate_gradient_magnitude()
    self.__calculate_gradient_direction()


  def __smooth_with_gaussian_kernel(self):
    self.result_img = apply_kernel_to_matrix(GAUSSIAN_KERNEL_5, self.img)


  def __calculate_gradient_with_sobel_kernels(self):
    self.gradient_x = apply_kernel_to_matrix(SOBEL_KERNEL_X, self.result_img)
    self.gradient_y = apply_kernel_to_matrix(SOBEL_KERNEL_Y, self.result_img)

  def __calculate_gradient_magnitude(self):
    powered_gradients_sum = np.power(self.gradient_x, 2) + np.power(self.gradient_y, 2)
    self.gradient_magnitude = np.sqrt(powered_gradients_sum)

  def __calculate_gradient_direction(self):
    gradient_direction_in_radians = np.arctan2(self.gradient_y, self.gradient_x)
    gradient_direction_in_degrees = gradient_direction_in_radians * 180 / pi
    self.gradient_direction = gradient_direction_in_degrees


  def get_result_img(self):
    if self.result_img is None:
      raise ValueError('No result image have been found. Call the apply_edge_detector method before.')

    return self.result_img
