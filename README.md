# Trabalho SO - Semáforos

Este projeto visa expor os problemas advindos do acesso concorrente de tarefas a estruturas de dados compartilhadas e compreender a coordenação dos acessos através de semáforos. Foi feito um programa com duas threads, que manipulam uma fila de inteiros de forma concorrente. Cada thread retira o primeiro elemento da fila e coloca um novo elemento no fim da fila como no exemplo abaixo:

```
Thread 1 -> ( Removido: 61 -- Inserido: 39 -- Fila: [26, 96, 70, 50, 78, 58, 10, 88, 72, 39] )

Thread 2 -> ( Removido: 26 -- Inserido: 70 -- Fila: [96, 70, 50, 78, 58, 10, 88, 72, 39, 70] )
```

Ao final, o programa mede o número de inserções de inteiros na fila por segundo.