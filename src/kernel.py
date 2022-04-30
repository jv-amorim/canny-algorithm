from math import floor

import numpy as np


def apply_kernel_to_matrix(kernel, matrix):
  kernel_applier = KernelApplier()
  kernel_applier.set_kernel(kernel)
  kernel_applier.set_input_matrix(matrix)
  kernel_applier.apply_kernel()
  return kernel_applier.get_result_matrix()


class KernelApplier:
  def set_kernel(self, kernel):
    self.k_height, self.k_width = kernel.shape

    if self.k_height != self.k_width:
      raise ValueError('The kernel matrix must have a square format (width == height)!')

    self.kernel = kernel
    self.k_radius =  floor(self.k_width / 2)

  def set_input_matrix(self, matrix):    
    self.matrix = matrix
    self.m_height, self.m_width = matrix.shape
    self.new_matrix = np.zeros(matrix.shape)

  def apply_kernel(self):
    if self.kernel is None:
      raise ValueError('The kernel matrix must be setted before calling this method.')
    if self.matrix is None:
      raise ValueError('The input matrix must be setted before calling this method.')

    for m_row_index in range(self.m_height - self.k_height + 1):
      for m_column_index in range(self.m_width - self.k_width + 1):
        center_value = self.__calculate_value_for_current_matrix_coords(m_row_index, m_column_index)
        row_center_index = m_row_index + self.k_radius
        column_center_index = m_column_index + self.k_radius
        self.new_matrix[row_center_index, column_center_index] = center_value

    self.__fill_not_covered_pixels()

  def get_result_matrix(self):
    return self.new_matrix

  def __calculate_value_for_current_matrix_coords(self, m_row_index, m_column_index):
    current_sum = 0

    for k_row_index in range(self.k_height):
      for k_column_index in range(self.k_width):
        current_m_value = self.matrix[m_row_index + k_row_index, m_column_index + k_column_index]
        current_k_value = self.kernel[k_row_index, k_column_index]
        current_sum += current_m_value * current_k_value

    return current_sum

  def __fill_not_covered_pixels(self):
    not_covered_rows = (
      list(range(self.k_radius))
      + list(range(self.m_height - self.k_radius, self.m_height))
    )
    not_covered_columns = (
      list(range(self.k_radius))
      + list(range(self.m_width - self.k_radius, self.m_width))
    )

    for row in not_covered_rows:
      self.new_matrix[row, :] = self.matrix[row, :]
    for column in not_covered_columns:
      self.new_matrix[:, column] = self.matrix[:, column]
