#include "queue.c"

int main(){
    Queue *q = create_queue(6);
    q->data[2] = 10;
    q->data[3] = 12;
    q->front = 2;
    q->rear = 3;
    print_queue(q);
    enqueue(q, 7);
    print_queue(q);
    dequeue(q);
    enqueue(q, 1);
    enqueue(q, 6);
    print_queue(q);

    Queue *q2 = create_queue(1);
    enqueue(q2, 1);
    enqueue(q2, 2);
    enqueue(q2, 3);
    enqueue(q2, 4);
    print_queue(q2);
    enqueue(q2, 5);
    print_queue(q2);

    Queue *q3 = create_queue(4);
    q3->front = 2;
    q3->rear = 2;
    enqueue(q3, 1);
    enqueue(q3, 2);
    enqueue(q3, 3);
    enqueue(q3, 4);
    print_queue(q3);
    enqueue(q3, 5);
    print_queue(q3);
}