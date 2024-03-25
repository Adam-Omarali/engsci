#include <stdio.h>
#include <stdlib.h>

typedef struct node{
    int data;
    struct node *next;
} node;

typedef struct LL{
    node *head;
} LL;

int len_ll(LL *list)
{
    int i = 1;
    if (list->head == NULL)
    {
        return 0;
    }
    node *elem = list->head;
    while (elem->next != NULL)
    {
        i++;
        elem = elem->next;
    }
    return i++;
}

int main()
{
    LL *list = (LL *)malloc(sizeof(LL));
    list->head = (node *)malloc(sizeof(node));
    list->head->data = 1;
    list->head->next = NULL;
    list->head->next->data = 2;
    list->head->next->next = (node *)malloc(sizeof(node));
    // list->head->next->next->data = 3;
    // list->head->next->next->next = NULL;
    printf("%d\n", len_ll(list));
    return 0;
}