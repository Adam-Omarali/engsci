/**
 * Implement a circular queue struct 
 * using an circular array with an initial capacity and dynamic resizing.
*/
#include <stdio.h>
#include <stdlib.h>

struct CircularQueue {
    int *arr;
    int capacity; // Note: capacity is the maximum number of elements 
                  // that the queue can hold, 
                  // not the current number of elements in the queue.
    int begin;
    int end;
};

void createCircularQueue(struct CircularQueue *q, int capacity) {
    q->arr = (int *)malloc(capacity * sizeof(int));
    q->capacity = capacity;
    q->begin = 0;
    q->end = 0; // This is consistent with Python indexing, 
                // but one more than the number printed in printQueue below.
}

void enqueue(struct CircularQueue *q, int value) {
    // Check if the queue is full
    if ((q->end + 1) % q->capacity == q->begin) {
        // Use realloc to double the size of the queue
        q->arr = (int *)realloc(q->arr, 2 * q->capacity * sizeof(int));
        // Copy the elements from the beginning to the end of the queue
        for (int i = 0; i < q->begin; i++) {
            q->arr[i + q->capacity] = q->arr[i];
        }
        q->end = q->capacity + q->end;
        q->capacity *= 2;
    }

    q->arr[q->end] = value;
    q->end = (q->end + 1) % q->capacity;
}

int dequeue(struct CircularQueue *q) {
    if (q->begin == q->end) {
        printf("Queue is empty\n");
        return -1;
    }
    int value = q->arr[q->begin];
    // q->arr[q->begin] = 0;
    q->begin = (q->begin + 1) % q->capacity;
    return value;
}

/**
 * Write a function that prints the circular queue in the following format:
    index 0 1 2 3 4 5
    10 12
    Begin at index: 2
    End at index: 3
    -----------------------------------
    After enqueue 7:
    index 0 1 2 3 4 5
    10 12 7
    Begin at index: 2
    End at index: 4
    -----------------------------------
    After dequeue:
    index 0 1 2 3 4 5
    12 7
    Begin at index: 3
    End at index: 4
*/

void printQueue(struct CircularQueue *q) {
    printf("Capacity: %d\n", q->capacity);
    printf("index\t");
    for (int i = 0; i < q->capacity; i++) {
        printf("%10d\t", i);
    }
    printf("\nmemory\t");
    for (int i = 0; i < q->capacity; i++) {
        if (q->arr[i] != 0) {
            printf("%10d\t", q->arr[i]);
        }
    }
    printf("\n");
    if (q->begin == q->end) {
        printf("Empty queue\n");
    } else {
        printf("Begin at index: %d\n", q->begin);
        printf("End at index: %d\n", (q->end - 1 + q->capacity) % q->capacity);
        printf("Number of elements: %d\n", (q->end - q->begin + q->capacity) % q->capacity);
        printf("Elements in the queue:\n");
        for (int i = q->begin; i != q->end; i = (i + 1) % q->capacity) {
            printf("%d ", q->arr[i]);
        }
        printf("\n");
    }
    printf("-----------------------------------\n");
}

int main() {
    struct CircularQueue q;
    createCircularQueue(&q, 4);
    printQueue(&q);
    printf("Dequeue: %d\n", dequeue(&q));
    enqueue(&q, 1);
    printQueue(&q);
    enqueue(&q, 2);
    printQueue(&q);
    enqueue(&q, 3);
    printQueue(&q);
    printf("Dequeue: %d\n", dequeue(&q));
    printQueue(&q);
    printf("Dequeue: %d\n", dequeue(&q));
    printQueue(&q);
    for (int i = 4; i < 10; i++) {
        enqueue(&q, i);
        printQueue(&q);
    }
    printf("Dequeue: %d\n", dequeue(&q));
    printQueue(&q);
    return 0;
}