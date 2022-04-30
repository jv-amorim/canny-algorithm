import numpy as np

# Input/Output:

INPUT_DIR = 'input/'
OUTPUT_DIR = 'output/'


# Gaussian Kernels:

# Obtained from:
# Shipitko, Oleg & Grigoryev, Anton. (2018). Gaussian filtering for FPGA based image processing with High-Level Synthesis tools. 
# https://www.researchgate.net/publication/325768087_Gaussian_filtering_for_FPGA_based_image_processing_with_High-Level_Synthesis_tools.

GAUSSIAN_KERNEL_3 = np.array([[1, 2, 1],
                              [2, 4, 2],
                              [1, 2, 1]]) / 16

GAUSSIAN_KERNEL_5 = np.array([[1,  4,  7,  4, 1],
                              [4, 16, 26, 16, 4],
                              [7, 26, 41, 26, 7],
                              [4, 16, 26, 16, 4],
                              [1,  4,  7,  4, 1]]) / 273

GAUSSIAN_KERNEL_7 = np.array([[0,  0,  1,   2,  1,  0, 0],
                              [0,  3, 13,  22, 13,  3, 0],
                              [1, 13, 59,  97, 59, 13, 1],
                              [2, 22, 97, 159, 97, 22, 2],
                              [1, 13, 59,  97, 59, 13, 1],
                              [0,  3, 13,  22, 13,  3, 0],
                              [0,  0,  1,   2,  1,  0, 0]]) / 1003


# Sobel Kernels:

SOBEL_KERNEL_X = np.array([[-1,  0,  1],
                           [-2,  0,  2], 
                           [-1,  0,  1]])

SOBEL_KERNEL_Y = np.array([[-1, -2, -1],
                           [ 0,  0,  0], 
                           [ 1,  2,  1]])
