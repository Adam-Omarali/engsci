#include <stdio.h>

void f(int b)
{
    b = 40; //this will not change the value of a since its a local variable
}

void f2(int *b){
    *b = 40; 
    //this does change it since you get a local variable of the memory address of a, 
    //but the value a will stay at the same memory address
}

void swap(int *a, int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}

int main()
{
    int a = 43;
    f(a);
    printf("%d\n", a);
    f2(&a);
    printf("%d\n", a);

    int b = 20;
    printf("a:%d, b: %d\n", a, b);
    swap(&a, &b);
    printf("a:%d, b: %d\n", a, b);

    const char *s = "Hello";
    s = "World";
    //s[0] = 'W'; //this will give an error since s is a pointer to a string literal
    printf("%s\n", s);

    char *k = "Hello";
    k = "World";
    //k[0] = 'W'; //still gives an error since char * is inherently const char *
    printf("%s\n", k);

    char t[] = "Hello";
    //t = "World"; //this will give an error since t is an array
    t[0] = 'W';
    printf("%s\n", t);

    return 0;
}