from consts import GAUSSIAN_KERNEL_5
from kernel import apply_kernel_to_matrix


def apply_canny_algorithm_to_image(img):
  smoothed_img = apply_kernel_to_matrix(GAUSSIAN_KERNEL_5, img)
  return smoothed_img
