#include <stdio.h>
#include <stdlib.h>

typedef struct queue
{
    int array[CAPACITY];
    int front;
    int size;
}
queue;

queue q;

void enqueue(queue *q, int data);
void dequeue(queue *q);

// next element to be removed
q.front = 0;
// length of the queue
q.size = 0;

for (int i = 0; i < q.size; i++)
{
    enqueue(&q, i);
    q.front = i;
}

void enqueue(queue *q, int data)
{
    q.array[q.size] = data;
    q.size++;
}

int dequeue(queue *q)
{
    int e = q[q.front];
    q.size--;
    return e;
}