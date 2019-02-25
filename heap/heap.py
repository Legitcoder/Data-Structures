from math import floor
class Heap:
  def __init__(self):
    self.storage = []

  def insert(self, value):
    self.storage.append(value)
    if len(self.storage) > 1:
      self._bubble_up(len(self.storage) - 1)
    print(self.storage)

  def delete(self):
    root = self.storage.pop(0)
    return root

  def get_max(self):
    return self.storage[0]

  def get_size(self):
    return len(self.storage)

  def _bubble_up(self, index):
    child = self.storage[index]
    parent = self.storage[floor((index - 1) / 2)]
    #If parent is less than child, swap
    if parent < child:
      self.storage[floor((index - 1) / 2)], self.storage[index] = self.storage[index], self.storage[floor((index - 1) / 2)]

  def _sift_down(self, index):
    p = (index-1)/2
    print(p)


heap = Heap()
heap.insert(6)
heap.insert(8)
heap.insert(10)
heap.insert(9)
heap.insert(1)
heap.insert(9)
heap.insert(9)
heap.insert(5)