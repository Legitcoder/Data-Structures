class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    if self is None: print("It's None")
    while self.value is not None:
      if self.value < value:
        pass
      elif self.value > value:
        pass

  def contains(self, target):
    pass

  def get_max(self):
    pass

bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
bst.insert(7)
bst.insert(6)
print(bst.left.right.value)
print(bst.right.left.value)