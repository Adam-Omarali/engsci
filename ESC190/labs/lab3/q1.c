#include <stdio.h>

void set_int1(int x)
{
    x = 42;
}

void set_int2(int *p_x)
{
    *p_x = 42;
}

int main()
{
    int a = 0;
    set_int1(a); //this will not change a because the value is copied when passed into the function
    printf("%d\n", a);
    set_int2(&a); //this will change since the memory address is copied, but a still lives at that memory address
    printf("%d\n", a);
}