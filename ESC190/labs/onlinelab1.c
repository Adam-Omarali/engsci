#include <stdio.h>
int linear_search(int *a, int sz, int elem)
{
    for (int i = 0; i < sz; i++)
    {
        if (a[i] == elem)
        {
            return i;
        }
    }
    return -1;
}

void reverse_arr(int *arr, int sz)
{
    for (int i = 0; i < (int)sz / 2; i++)
    {
        int temp = arr[i];
        arr[i] = arr[sz - i - 1];
        arr[sz - i - 1] = temp;
    }
    // for (int i = 0; i < sz; i++)
    // {
    //     printf("%d", arr[i]);
    // }
    // printf("\n");
}

int main()
{
    int arr[] = {5, 6, 7, 8, 9};

    int idx = linear_search(arr, sizeof(arr) / sizeof(int), 7);
    // printf("%d\n", idx);
    reverse_arr(arr, sizeof(arr) / sizeof(int));
}