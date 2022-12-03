import threading, random, time
from CircularQueue import CircularQueue

def interaction_queue(queue, results):
    quantity = 0
    timeStart = time.time()
    
    while True:
        elementRemove = queue.dequeue()
        elementInsert = random.randint(1,100)
        queue.enqueue(elementInsert)
        quantity += 1
        
        print(f'( Removido: {elementRemove} -- Inserido: {elementInsert} -- Fila: {queue.final_queue} )')
        print()
        
        timeEnd = time.time()
        if timeEnd-timeStart >= 1:
            break

    results['Serial'] = {'Quantidade': quantity}
           
def run_algorithm():
    queue = CircularQueue(10)
    results = {}
    
    #Adicionando elementos na fila
    for _ in range(10):
        queue.enqueue(random.randint(1,100))
    
    print(f'Fila Inicial: {queue.final_queue}')
    print()
    
    interaction_queue(queue, results)
    
    result = results['Serial']['Quantidade']
    print(f'Quantidade de inserções de inteiros na fila por segundo no algoritmo serial: {result}\n')

run_algorithm()