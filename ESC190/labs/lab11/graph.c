#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int** matrix()
{
    int **adj_matrix = (int **)malloc(sizeof(int *) * 5);
    for (int i = 0; i < 6; i++)
    {
        adj_matrix[i] = (int *)malloc(sizeof(int) * 5);
        for (int k = 0; k < 6; k++)
        {
            adj_matrix[i][k] = 0;
        }
    }
    adj_matrix[0][2] = 1;
    adj_matrix[0][5] = 1;

    adj_matrix[1][2] = 1;
    adj_matrix[1][4] = 1;

    adj_matrix[2][0] = 1;
    adj_matrix[2][1] = 1;
    adj_matrix[2][3] = 1;
    adj_matrix[2][4] = 1;

    adj_matrix[3][2] = 1;
    adj_matrix[3][4] = 1;

    adj_matrix[4][1] = 1;
    adj_matrix[4][5] = 1;

    adj_matrix[5][0] = 1;
    adj_matrix[5][4] = 1;

    return adj_matrix;
}

void *bfs(int **graph)
{
    int visited[6] = {0, 0, 0, 0, 0, 0};
    int added[6] = {0, 0, 0, 0, 0, 0};
    int *queue = (int *)malloc(sizeof(int) * 6);
    queue[0] = 1;
    int front = 0;
    int back = 1;

    while(queue[front] != NULL)
    {
        int curr = queue[front];
        printf("%d\n", curr);
        visited[curr - 1] = 1;
        added[curr - 1] = 0;
        front++;
        for (int k = 0; k < 6; k++)
        {
            if (graph[curr - 1][k] == 1 & !visited[k] & !added[k])
            {
                queue[back] = k+1;
                added[k] = 1;
                back++;
            }
        }
    }
}

void *dfs(int **graph)
{
    int visited[6] = {0, 0, 0, 0, 0, 0};
    int added[6] = {0, 0, 0, 0, 0, 0};
    int *stack = (int *)malloc(sizeof(int) * 6);
    stack[0] = 1;
    int top = 0;

    while(stack[top] != NULL)
    {
        int curr = stack[top];
        top--;
        printf("%d\n", curr);
        visited[curr - 1] = 1;
        added[curr - 1] = 0;
        for (int k = 0; k < 6; k++)
        {
            if (graph[curr - 1][k] == 1 & !visited[k] & !added[k])
            {
                top++;
                stack[top] = k+1;
                added[k] = 1;
            }
        }
    }
}

int main()
{
    int **graph = matrix();
    printf("bfs");
    bfs(graph);
    printf("dfs");
    dfs(graph);

    return 0;
}