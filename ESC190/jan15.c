#include <stdio.h>

//passing in an address
//copy the value of the local value to the function call, won't copy make a new address like in python
int f(int *p){
    //function goes in and modifies the value of the address
    *p = 43;
    return *p;
    //*p the value at p
    //p is the pointer (address of &a)
    //&p is the address of p itself
}

int main(){
    int a = 43;
    int x = f(&a);
    int b = &a; //turns pointer into integer by ... autocasting?
    printf("%d\n", x);
    // printf("%ld\n", *b); //* is an operand which only works on pointers (data types including a *)

    char *h = "hello";
    printf("%s is stored at %ld\n", h, (long int)h); //casting gives no warning


    int arr[] = {5, 6, 7};
    printf("%ld\n", arr); //print the address where the array starts
                            //equal to the addresss of 5
                            //is arr and &arr the same thing?
                            //yes is arr is the address of where the array starts and &arr -> &(a+0)
    printf("%d\n", *arr); //prints the value 5 by going to the address of 5

    return 0;
}


//when saying a[0] -> this really means *(a+0)