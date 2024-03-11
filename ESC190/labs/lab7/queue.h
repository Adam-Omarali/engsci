#include <stdio.h>
#include <stdlib.h>

typedef struct Queue {
    int *data;
    int front;
    int rear;
    int size;
    int elements;
} Queue;

Queue *create_queue(int size);
void enqueue(Queue *q, int new_elem);
void dequeue(Queue *q);
void print_queue(Queue *q);
void just_print(Queue *q);
