#include <stdio.h>

void print_arr(int arr[], unsigned long arr_size){
    for (int i = 0; i < arr_size; i++)
    {   
        printf("%d", arr[i]);
    }
    printf("\n");
}

int main()
{
    int arr[5] = {2, 5, 3, 4, 1};
    int i = 0;
    while (i < sizeof(arr) / sizeof(arr[0])){
        int j = i ;
        while (j >= 0 && arr[j+1] < arr[j])
        {
            int temp = arr[j];
            arr[j] = arr[j+1];
            arr[j+1] = temp;
            j--;
        }
        i++;
    }
    print_arr(arr, sizeof(arr) / sizeof(arr[0]));
    return 0;
}