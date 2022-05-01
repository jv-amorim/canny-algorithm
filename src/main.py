from canny import apply_canny_edge_detector_to_img
from input_output import get_input_img_name_from_arguments, read_input_img, save_output_img
from utils import ImageUtils


def main():
  input_img_name = get_input_img_name_from_arguments()
  bgr_input_img = read_input_img(input_img_name)

  result_img = ImageUtils.convert_bgr_img_to_grayscale(bgr_input_img)
  result_imgs = apply_canny_edge_detector_to_img(result_img)

  save_output_img(result_imgs.smoothed, '_output-step-1.png')
  save_output_img(result_imgs.gradient_x, '_output-step-2.png')
  save_output_img(result_imgs.gradient_y, '_output-step-3.png')
  save_output_img(result_imgs.gradient_magnitude, '_output-step-4.png')
  save_output_img(result_imgs.nonmaximum_suppressed, '_output-step-5.png')
  save_output_img(result_imgs.thresholded, 'output-detected-edges.png')


if __name__ == '__main__':
  main()
