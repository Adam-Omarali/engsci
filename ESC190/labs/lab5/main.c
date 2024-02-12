#include "intlist.h"
#include <stdio.h>

int main()
{
    IntList *list;
    int data[] = {5, 4, 3, 2, 1};

    create_list_from_data(&list, data, sizeof(data));
    printf("Add data\n"); 
}