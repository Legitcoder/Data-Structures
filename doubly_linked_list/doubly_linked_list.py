"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
  def __init__(self, value, prev=None, next=None):
    self.value = value
    self.prev = prev
    self.next = next

  """Wrap the given value in a ListNode and insert it
  after this node. Note that this node could already
  have a next node it is point to."""
  def insert_after(self, value):
    current_next = self.next
    self.next = ListNode(value, self, current_next)
    if current_next:
      current_next.prev = self.next

  """Wrap the given value in a ListNode and insert it
  before this node. Note that this node could already
  have a previous node it is point to."""
  def insert_before(self, value):
    current_prev = self.prev
    self.prev = ListNode(value, current_prev, self)
    if current_prev:
      current_prev.next = self.prev

  """Rearranges this ListNode's previous and next pointers
  accordingly, effectively deleting this ListNode."""
  def delete(self):
    if self.prev:
      self.prev.next = self.next
    if self.next:
      self.next.prev = self.prev

"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node

  def add_to_head(self, value):
    if self.head is None and self.tail is None:
      self.head = ListNode(value)
      self.tail = self.head
      self.tail.next = None
      self.tail.prev = None
      self.head.next = None
      self.head.prev = None
      return

    if self.head is self.tail:
      self.head = None
      list_node = ListNode(value)
      self.tail.prev = self.head
      self.head = list_node
      self.head.next = self.tail
      return


    list_node = ListNode(value)
    new_next = self.head
    self.head.prev = list_node
    self.head = self.head.prev
    self.head.next = new_next

  def remove_from_head(self):
    deleted_head = self.head
    self.delete(self.head)
    return deleted_head.value

  def add_to_tail(self, value):
    if self.head is None and self.tail is None:
      self.head = ListNode(value)
      self.tail = self.head
      self.tail.next = None
      self.tail.prev = None
      self.head.next = None
      self.head.prev = None
      return

    if self.head is self.tail:
      self.tail = None
      list_node = ListNode(value)
      self.tail = list_node
      self.tail.prev = self.head
      self.head.next = self.tail
      return

    list_node = ListNode(value)
    self.tail.next = list_node
    list_node.prev = self.tail
    self.tail = self.tail.next

  def remove_from_tail(self):
    deleted_tail = self.tail
    self.tail.delete()
    return deleted_tail.value


  def move_to_front(self, node):
    node.delete()
    self.add_to_head(node.value)
    return self.head.value

  def move_to_end(self, node):
    node.delete()
    self.add_to_tail(node.value)
    return self.head.value

  def delete(self, node):
    if node.next is None and node.prev is None and self.head is node and self.tail is node:
      self.head = None
      self.tail = None
      return
    #This is the head
    if node.prev is None and node.next is not None:
      self.head = node.next


    #This is the tail
    if node.next is None and node.prev is not None:
      self.tail = node.prev

    node.prev = self.head
    if node.next is not None: self.head = node.next
    if node.next.next is not None: self.head.next = node.next.next

    
  def get_max(self):
    maximum = float("-inf")
    head = self.head
    while head is not None:
      if head.value > maximum: maximum = head.value
      head = head.next
    return maximum
