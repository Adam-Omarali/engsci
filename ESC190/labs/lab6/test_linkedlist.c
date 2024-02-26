#include "linkedlist.c"
#include <stdio.h>

int main()
{
    LL *linkedlist = (LL *)malloc(sizeof(LL) * 2);
    linkedlist->size = 2;
    node *n1 = (node *)malloc(sizeof(node));
    node *n2 = (node *)malloc(sizeof(node));

    n1->data = 3;
    n1->next = n2;
    n2->data = 4;
    n2->next = NULL;
    linkedlist->head = n1;

    print_LL(linkedlist);
    LL_append(linkedlist, 5);
    printf("%d\n", linkedlist->size);
    print_LL(linkedlist);
    printf("%d\n", validate_list_length(linkedlist));

    delete_elem(linkedlist, 2);
    print_LL(linkedlist);
    delete_elem(linkedlist, 0);
    print_LL(linkedlist);

    free(linkedlist);
}
