#include "intlist.h"
#include <stdlib.h>
#include <string.h>

// Allocate memory for an object of type IntList, initialize
// its data to equal the data in data_arr, and set its size
// Store the address of the new object in *p_IntList
void create_list_from_data(IntList **p_IntList, int *data_arr, int size)
{
    IntList *temp = (IntList *)malloc(sizeof(int) * size);
    temp->data = data_arr;
    temp->size = sizeof(int) * size;
    temp->capacity = sizeof(int) * size;
    *p_IntList = temp;

}

// Append new_elem to the end of list
void list_append(IntList *list, int new_elem)
{
    list->size = list->size + sizeof(int);
    //if capacity is too small, 
    if(list->size + sizeof(int) < list->capacity)
    {
        realloc(list->data, list->size);
        list->capacity = list->size;
    }
    list->data[list->size - 1] = new_elem;
}

// Insert new_elem at index in list. new_elem should now be at
// location index.
// Use the function memmove to move elements of list->data as needed
// If the capacity needs to grow, use realloc to increase the capacity by
// a factor of 2
void list_insert(IntList *list, int new_elem, int index)
{
    list->size = list->size + sizeof(int);
    if(list->size + sizeof(int) < list->capacity)
    {
        realloc(list->data, list->capacity * 2);
        list->capacity = list->capacity * 2;
    }
    memmove((list->data + index + 1), (list->data + index), list->size - index);

}

// Delete the element at index index

void list_delete(IntList *list, int index)
{
    memmove(list->data + index + 1, list->data + index, list->size - index);
    list->size = list->size - sizeof(int);
}

// call free as appropriate to free the memory used by list
// Note: the order in which you free list->data and list
// itself is important (how?)
void list_destroy(IntList *list)
{
    free(list->data);
    free(list);
}

// Return the element at index index in list
int list_get(IntList *list, int index)
{
    return list->data[index];
}
