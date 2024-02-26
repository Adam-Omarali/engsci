#include "node.h"

void print_LL(LL *my_list){
    node *elem = my_list->head;
    while (elem->next != NULL){
        printf("%d\n", elem->data);
        elem = elem->next;
    }
    printf("%d\n", elem->data);
}

void LL_append(LL *my_list, int new_elem){
    node *new_node = (node *)malloc(sizeof(node));
    new_node->data = new_elem;
    new_node->next = NULL;

    node *elem = my_list->head->next;

    int i = 1;
    while (elem->next != NULL){
        elem = elem->next;
        i++;
    }
    i = i + 2; //for new element and null element
    my_list->size = i;
    elem->next = new_node;
}

int validate_list_length(LL *my_list)
{
    int i = 1;
    node * elem = my_list->head;
    while(elem->next != NULL){
        elem = elem->next;
        i++;
    }
    i++; //for the null element
    return i == my_list->size;
}

void delete_elem(LL *my_list, int idx){
    int i = 0;
    node * elem = my_list->head;
    if (idx > my_list->size)
    {
        printf("idx is out of bounds");
        exit(1);
    }
    while(i < idx - 1){
        elem = elem->next;
        i++;
    }

    node *elem_to_delete;
    //edge case
    if (idx == 0){
        elem_to_delete = elem;
        my_list->head = elem_to_delete->next;
    }
    else{
        elem_to_delete = elem->next;
        if (elem_to_delete->next == NULL){
            elem->next = NULL;
        }
        else{
            elem->next = elem_to_delete->next;
        }
    }

    my_list->size--;
    free(elem_to_delete);
}