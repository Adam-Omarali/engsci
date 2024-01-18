#include <stdio.h>

void f(int *a) //same as int a[] when passing into a function (both compile to the address of the first element of a)
{
    printf("%ld\n", sizeof(a) / sizeof(a[0]));
}

void f2(int a[]){
    printf("%ld\n", sizeof(a) / sizeof(a[0])); //no difference
}

int main()
{
    int arr[] = {5, 3, 4, 1};
    //TODO: how is this actually stored so the program knows how to compute size of, especially if int a[] is the same type???
    sizeof(arr); //total number of memory cells occupied by the array (in this case 4 numbers * 4 bytes / number)

    int *p_a0 = arr;
    sizeof(p_a0); //the number of memory cells occupied by an address

    f(arr);
    f2(arr);

    return 0;
}