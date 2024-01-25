#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int *f()
{
    int arr[20];
    arr[0] = 42;
    return arr;
}

int *make_block_int(int sz)
{
    int *p = (int *)malloc(sz * sizeof(int));
    if (p == NULL) //if there is not enough memory for malloc
    {
        printf("Error: malloc failed\n");

        exit(1); //better to exit 1 so the program does not proceed and potentially perform operations that set it on fire
    }
    return p;
}

int main()
{
    int *p_arr = f();
    // printf("%d\n", p_arr[0]); // undefined behaviour, may print 42, may burn the computer
    //the problem is the address of p_arr pointed to a local variable within the function
    //so after the function is called, that memory space can be used for other things

    int *q = make_block_int(100); //memory from malloc will stay allocated until free or the program stops
    //therefore doesn't matter it's defined locally in a function
    q[0] = 42; // works


    char s1[] = "hi";
    char *s2;

    //strcpy(s2, s1); //not okay since s2 doesn't have an address the function can go to
    s2 = s1; //s2 points to the first address of s1 (they are aliases)

    s2 = (char *)malloc(sizeof(char) * (strlen(s1) + 1)); //s2 now points to a new memory space
    strcpy(s2, s1); //now okay since s2 has an address given by malloc
}