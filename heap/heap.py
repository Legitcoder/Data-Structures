from math import floor
class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    if len(self.storage) > 0:
      self._bubble_up(len(self.storage) - 1)

  def delete(self):
    previous_root = self.storage[0]
    element = self.storage.pop()
    if len(self.storage) > 0:
      self.storage[0] = element
      self._sift_down(0)
    return previous_root


  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    child = self.storage[index]
    parent = self.storage[floor((index - 1) / 2)]
    #print(f'{self.storage} parent: {parent}, child: {child}')
    #If parent is less than child, swap
    while parent < child:
      self.storage[floor((index - 1) / 2)], self.storage[index] = self.storage[index], self.storage[floor((index - 1) / 2)]
      index = floor((index - 1) / 2)
      if index > 0:
        parent = self.storage[floor((index - 1) / 2)]
      else:
        break

  def get_left_child(self, index):
    n = (2 * index) + 1
    if n < len(self.storage):
      return self.storage[n]
    return float("-inf")

  def get_right_child(self, index):
    n = (2 * index) + 2
    if n < len(self.storage):
      return self.storage[n]
    return float("-inf")

  def _sift_down(self, index):
    current_node = self.storage[index]
    left = self.get_left_child(index)
    right = self.get_right_child(index)
    while current_node < left or current_node < right:
      #print(f'{current_node} > {left} and {right}')
      if left > current_node and left >= right:
        self.storage[(2 * index) + 1], self.storage[index] = self.storage[index], self.storage[(2*index) + 1]
        index = (2 * index) + 1
        current_node = self.storage[index]
        left = self.get_left_child(index)
        right = self.get_right_child(index)
      elif right > current_node and right >= left:
        self.storage[(2 * index) + 2], self.storage[index] = self.storage[index], self.storage[(2*index) + 2]
        index = (2 * index) + 2
        current_node = self.storage[index]
        left = self.get_left_child(index)
        right = self.get_right_child(index)