import threading, random, time
from CircularQueue import CircularQueue

def interaction_queue(name_thread, semaphore, queue, results):
    quantity = 0
    timeStart = time.time()
    
    while True:
        semaphore.acquire()
        elementRemove = queue.dequeue()
        elementInsert = random.randint(1,100)
        queue.enqueue(elementInsert)
        quantity += 1
        
        print(f'{name_thread} -> ( Removido: {elementRemove} -- Inserido: {elementInsert} -- Fila: {queue.final_queue} )')
        print()
        
        timeEnd = time.time()
        if timeEnd-timeStart >= 1:
            semaphore.release()
            break
        semaphore.release()

    results[name_thread] = {'Quantidade': quantity}
           
def run_algorithm():
    semaphore = threading.Semaphore(2)
    queue = CircularQueue(10)
    results = {}
    
    #Adicionando elementos na fila
    for _ in range(10):
        queue.enqueue(random.randint(1,100))
    
    print(f'Fila Inicial: {queue.final_queue}')
    print()
            
    t1 = threading.Thread(target=interaction_queue, args = ["Thread 1", semaphore, queue, results])
    t2 = threading.Thread(target=interaction_queue, args = ["Thread 2", semaphore, queue, results])

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    
    total_per_second = 0
    for key in results.keys():
        total_per_second += results[key]['Quantidade']
    print(f'Quantidade de inserções de inteiros na fila por segundo no algoritmo concorrente: {total_per_second}\n')

run_algorithm()