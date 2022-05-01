from canny import apply_canny_edge_detector_to_img
from input_output import get_command_line_arguments, read_input_img, save_output_img
from utils import ImageUtils


def main():
  (input_img_name, low_threshold, high_threshold) = get_command_line_arguments()

  print('Reading the input image...')
  bgr_input_img = read_input_img(input_img_name)

  print('Converting the image to grayscale...')
  gray_input_img = ImageUtils.convert_bgr_img_to_grayscale(bgr_input_img)

  result_imgs = apply_canny_edge_detector_to_img(gray_input_img, low_threshold, high_threshold)

  print('Saving the output images...')
  save_output_img(result_imgs.smoothed, '_output-step-1.png')
  save_output_img(result_imgs.gradient_x, '_output-step-2.png')
  save_output_img(result_imgs.gradient_y, '_output-step-3.png')
  save_output_img(result_imgs.gradient_magnitude, '_output-step-4.png')
  save_output_img(result_imgs.nonmaximum_suppressed, '_output-step-5.png')
  save_output_img(result_imgs.thresholded, 'output-detected-edges.png')

  print('Finished with success!')


if __name__ == '__main__':
  main()
