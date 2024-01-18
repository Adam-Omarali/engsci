#include <stdio.h>

//order of function decleration matters
void print_arr(int arr[], unsigned long arr_size){
    for (int i = 0; i < arr_size; i++)
    {   
        printf("%d", arr[i]);
    }
    printf("\n");
}

void seq_replace(int *arr1, unsigned long arr1_sz, int *arr2, unsigned long arr2_sz)
{
    for (int i = 0; i < arr2_sz; i++)
    {
        int element = arr2[i];
        for (int k = 0; k < arr1_sz; k++)
        {
            if(arr1[k] == element){
                arr1[k] = 0;
            }
        }
    }
    print_arr(arr1, arr1_sz);
    //run time complexity is len(arr_1) * len(arr_2)
}


int main()
{
    int a[] = {5, 6, 7, 8, 6, 7};
    int b[] = {6, 7};
    seq_replace(a, 6, b, 2);
    return 0;
}