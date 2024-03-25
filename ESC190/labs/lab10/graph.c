#include "ll.c"
#include <stdlib.h>
#include <stdio.h>

// # 1 -> 2 -> 3
// # 2 -> 5
// # 3 -> 4
// # 4 ->
// # 5 ->

LL** construct_graph()
{
    LL *one = (LL *)malloc(sizeof(LL));
    one->head = (node *)malloc(sizeof(node));
    one->head->data = "1";
    one->size = 1;
    LL_append(one, "2");
    LL_append(one, "3");

    LL *two = (LL *)malloc(sizeof(LL));
    two->head = (node *)malloc(sizeof(node));
    two->head->data = "2";
    two->head->next = NULL;
    two->size = 1;
    LL_append(two, "5");

    LL *three = (LL *)malloc(sizeof(LL));
    three->head = (node *)malloc(sizeof(node));
    three->head->data = "3";
    three->head->next = NULL;
    three->size = 1;
    LL_append(three, "4");

    LL *four = (LL *)malloc(sizeof(LL));
    four->head = (node *)malloc(sizeof(node));
    four->head->data = "4";
    four->head->next = NULL;
    four->size = 1;

    LL *five = (LL *)malloc(sizeof(LL));
    five->head = (node *)malloc(sizeof(node));
    five->head->data = "5";
    five->head->next = NULL;
    five->size = 1;

    LL **graph = (LL **)malloc(sizeof(LL) * 5);
    graph[0] = one;
    graph[1] = two;
    graph[2] = three;
    graph[3] = four;
    graph[4] = five;
    return graph;
}

int get_ind_from_str(char *str, char **strs)
{
    for (int i = 0; i < 5; i++)
    {
        if (str == strs[i])
        {
            return i;
        }
    }
    return -1;
}

int are_linked(LL **graph, char *elem1, char *elem2, char **strs)
{
    node *elem = graph[get_ind_from_str(elem1, strs)]->head;
    node *node2 = graph[get_ind_from_str(elem2, strs)]->head;
    while (elem != NULL)
    {
        if (elem->data == node2->data)
        {
            return 1;
        }
        elem = elem->next;
    }
    return 0;
}

int** construct_adjacency_matrix_from_adjacency_list(LL **graph, int graph_size, char **strs)
{
    int **adj_matrix = (int **)malloc(sizeof(int *) * graph_size);
    for (int i = 0; i < graph_size; i++)
    {
        adj_matrix[i] = (int *)malloc(sizeof(int) * graph_size);
        node *elem = graph[i]->head;
        for (int j = 0; j < graph_size; j++)
        {
            if (i == j)
            {
                adj_matrix[i][j] = 1000000;
            }
            else
            {
                node *elem2 = graph[j]->head;
                int linked = are_linked(graph, elem->data, elem2->data, strs);
                adj_matrix[i][j] = linked;
            }
        }
    }
    return adj_matrix;
}

void print_adj_matrix(int **adj_matrix, int graph_size)
{
    for (int i = 0; i < graph_size; i++)
    {
        for (int j = 0; j < graph_size; j++)
        {
            printf("%d ", adj_matrix[i][j]);
        }
        printf("\n");
    }
}

int main()
{
    LL **graph = construct_graph();
    char *strs[5] = {"1", "2", "3", "4", "5"};
    printf("%d\n", are_linked(graph, "1", "5", strs)); // should print 1
    int **matrix_graph = construct_adjacency_matrix_from_adjacency_list(graph, 5, strs);
    print_adj_matrix(matrix_graph, 5);
}