import cv2
import sys
from consts import INPUT_DIR, OUTPUT_DIR


def get_command_line_arguments():
  arguments = sys.argv[1:]

  if len(arguments) < 1 or len(arguments) > 3:
    raise ValueError('Incorrect number of arguments.')

  input_img_name = arguments[0]
  low_threshold = None
  high_threshold = None

  if len(arguments) > 1:
    low_threshold = int(arguments[1])
  if len(arguments) > 2:
    high_threshold = int(arguments[2])

  return (input_img_name, low_threshold, high_threshold)

def read_input_img(input_img_name):  
  input_img = cv2.imread(INPUT_DIR + input_img_name)

  if input_img is None:
    raise ValueError('Input image file not found.')

  return input_img

def save_output_img(output_img, output_img_name):
  cv2.imwrite(OUTPUT_DIR + output_img_name, output_img)
