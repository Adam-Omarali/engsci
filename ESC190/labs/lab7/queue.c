#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "queue.h"

Queue *create_queue(int size){
    Queue *q = (Queue *)malloc(sizeof(Queue));
    q->data = (int *)malloc(size * sizeof(int));
    q->front = 0;
    q->rear = -1; 
    q->size = size;
    q->elements = 0;
    return q;
}

void enqueue(Queue *q, int new_elem){
    if(q->rear + 1 < q->size){
        q->rear++;
    }
    else{
        q->rear = 0;
    }
    q->elements++;
    if(q->elements >= q->size){
        q->data = (int *)realloc(q->data, 2 * q->size * sizeof(int));
        if(q->front > q->rear){
            // for (int i = 0; i < q->front; i++){
            //     q->data[i + q->size] = q->data[i];
            // }
            // just_print(q);
            // q->rear = q->size + q->front;
            memmove(q->data + q->size, q->data, sizeof(int) * q->rear);
            q->rear += q->size;
        }
        q->size *= 2;
    }
    q->data[q->rear] = new_elem;
}

void dequeue(Queue *q){
    int front_elem = q->data[q->front];
    q->data[q->front] = NULL;
    // free(q->data + q->front * sizeof(int)); not right

    if (q->front + 1 < q->size){
        q->front++;
    }
    else{
        q->front = 0;
    }
}

void just_print(Queue *q){
    for (int i = 0; i < q->size; i++){
        printf("%d ", q->data[i]);
    }
    printf("\n");
}

void print_queue(Queue *q){
    int i = q->front;
    while(i != q->rear){
        printf("%d -> ", q->data[i]);
        if(i + 1 < q->size){
            i++;
        }
        else{
            i = 0;
        }
    }
    printf("%d \n", q->data[q->rear]);
}
