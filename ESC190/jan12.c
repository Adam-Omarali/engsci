#include <stdio.h>

int main()
{
   printf("Hello, world!\n");

    //declared (create a memory address for hi) but not initialized (given a value)
   char *hi = "hi!";
   //put "hi!" in memory with the null character "/0". The null character tells the computer where it stops
   //store the address of h in hi
   //strings have to be double quotes, chars have to be single quotes

   printf("%s\n", hi); 
   // print hi by continusouly printing letters starting at the address of h until it reaches the null character, 
   //it knows to do this because the data type of hi is char *

   //%s - string, %d - integer, %ld - long decimal
   printf("%ld\n", hi); //will know to print the memory of address

   printf("the value of hi is: %s. The address is %ld\n", hi, hi);

   //seg fault -> trying to access or modify the memory table in a way that's incorrect
   int a = 43;
   printf("a value: %d\n", a);
   printf("a address: %d\n", &a); //this may return a negative number due to integer overflow!!!!
    //printf("%s\n", a); segfault

    double d = 3.14;
    printf("%f\n", d);

    int *pa = &a; //store the address of an integer a at pa
    printf("pa value: %ld\n", pa);
    printf("pa address %ld\n", &pa);
    printf("value of a from address of pa: %d\n", *pa);

    int *d_address = &d;
    printf("d_address: %ld\n", d_address);

    char *s1 = "hello!";
    //this star is apart of the datatype char *
    char c = *s1; //get value at address s1 (aka "h"), and store it at c
    //this star is used as a dereferencing operator - "get the value at the given address"

   return 0;
}