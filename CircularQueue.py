class CircularQueue():
  def __init__(self, k):
    self.k = k
    self.queue = [None] * k
    self.head = self.tail = -1
    self.final_queue = []

  def enqueue(self, data):
    if ((self.tail + 1) % self.k == self.head):
      print("The circular queue is full\n")

    elif (self.head == -1):
      self.head = 0
      self.tail = 0
      self.queue[self.tail] = data
    else:
      self.tail = (self.tail + 1) % self.k
      self.queue[self.tail] = data
    
    self.get_final_queue()

  def dequeue(self):
    if (self.head == -1):
      print("The circular queue is empty\n")

    elif (self.head == self.tail):
      temp = self.queue[self.head]
      self.head = -1
      self.tail = -1
      return temp
    else:
      temp = self.queue[self.head]
      self.head = (self.head + 1) % self.k
      return temp
    
    self.get_final_queue()

  def get_final_queue(self):
    self.final_queue = []
    
    if (self.tail >= self.head):
      for i in range(self.head, self.tail + 1):
        self.final_queue.append(self.queue[i])
    else:
      for i in range(self.head, self.k):
        self.final_queue.append(self.queue[i])
      for i in range(0, self.tail + 1):
        self.final_queue.append(self.queue[i])