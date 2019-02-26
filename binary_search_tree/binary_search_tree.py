class BinarySearchTree:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

  def insert(self, value):
    node = self
    #Traverse through Tree
    while node.value is not None:
      #If smaller than root traverse left
      if node.value > value:
        if node.left is None:
          node.left = BinarySearchTree(value)
          node = node.left
          break
        node = node.left
      #If larger than root traverse right
      if node.value < value:
        if node.right is None:
          node.right = BinarySearchTree(value)
          node = node.right
          break
        node = node.right


  def contains(self, target):
    node = self
    if node.value == target: return True
    while node is not None:
      if node.value > target:
        node = node.left
        if node is None:
          return False
          break
        if node.value == target: return True
      if node.value < target:
        node = node.right
        if node is None:
          return False
          break
        if node.value == target: return True


  def get_max(self):
    pass

bst = BinarySearchTree(5)
bst.insert(2)
bst.insert(3)
print(bst.value)
bst.insert(7)
bst.insert(6)
print(bst.left.value)
print(bst.right.value)
print(bst.right.left.value)
print(bst.left.right.value)