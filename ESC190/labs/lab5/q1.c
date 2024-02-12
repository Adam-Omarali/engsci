#include "intlist1.c"
#include <stdio.h>
#include <stdlib.h>

void print_arr(int *arr, int size)
{
    for(int i = 0; i < size; i++)
    {
        printf("%d, ", arr[i]);
    }
    printf("\n");
}

int main()
{
    IntList *list;
    int data[] = {5, 4, 3, 2, 1};

    create_list_from_data(&list, data, sizeof(data));
    print_arr(list->data, list->size / sizeof(int));

    list_append(list, 0);
    print_arr(list->data, list->size / sizeof(int));

    list_insert(list, 6, 0);
    print_arr(list->data, list->size / sizeof(int));
}