import threading, random, time

semaforo = threading.Semaphore(2)

class MyCircularQueue():

    def __init__(self, k):
        self.k = k
        self.queue = [None] * k
        self.head = self.tail = -1

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

    def printCQueue(self):
        if(self.head == -1):
            print("No element in the circular queue")

        elif (self.tail >= self.head):
            for i in range(self.head, self.tail + 1):
                print(self.queue[i], end=" ")
            print()
        else:
            for i in range(self.head, self.k):
                print(self.queue[i], end=" ")
            for i in range(0, self.tail + 1):
                print(self.queue[i], end=" ")
            print()

def interactionQueue(name_thread):
    i = 0
    semaforo.acquire()
    while i < 5:
        elementRemove = obj.dequeue()
        elementInsert = random.randint(1,100)
        obj.enqueue(elementInsert)
        print(name_thread + " -> Removido: " + str(elementRemove) + " Inserido: " + str(elementInsert))
        obj.printCQueue()
        time.sleep(0.5)
        i += 1   
    semaforo.release()

obj = MyCircularQueue(10)

j = 0
#Adicionando elementos na fila
while j < 10:
    obj.enqueue(random.randint(1,100))
    j += 1
    
obj.printCQueue()
        
t1 = threading.Thread(target=interactionQueue, args = ["Thread 1"])
t2 = threading.Thread(target=interactionQueue, args = ["Thread 2"])

t1.start()
t2.start()

t1.join()
t2.join()