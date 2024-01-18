#include <stdio.h>

void f(int *p_a)
{
    *p_a = 10;
}

void change_arr(char p_arr[], unsigned long arr_size)
{
    for (int i = 0; i < arr_size; i++)
    {
        p_arr[i] = 's';
    }
}

int main()
{
    int a = 5;
    f(&a);
    printf("%d\n", a);

    char arr[100];
    change_arr(arr, *(&arr + 1) - arr);
    printf("length: %d\n", *(&arr + 1) - arr);
    printf("%c\n", arr[0]);

    return 0;
}