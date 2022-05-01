import cv2
import sys
from consts import INPUT_DIR, OUTPUT_DIR


def get_input_img_name_from_arguments():
  arguments = sys.argv[1:]

  if len(arguments) != 1:
    raise ValueError('Incorrect number of arguments.')

  input_img_name = arguments[0]

  return input_img_name

def read_input_img(input_img_name):  
  input_img = cv2.imread(INPUT_DIR + input_img_name)

  if input_img is None:
    raise ValueError('Input image file not found.')

  return input_img

def save_output_img(output_img, output_img_name):
  cv2.imwrite(OUTPUT_DIR + output_img_name, output_img)
