#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct node{
    int data;
    struct node *next;
} node;

typedef struct LL{
    node *head;
    int size;
} LL;
// append integer new_elem to linked list my_list
void LL_append(LL *my_list, int new_elem);