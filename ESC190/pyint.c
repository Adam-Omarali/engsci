#include <stdlib.h>
#include <stdio.h>
#include "pyint.h"


void create_pyint(pyint **p, int length)
{
    *p = (pyint *)malloc(sizeof(pyint));
    (**p).buffer = (int *)malloc(length * sizeof(int));
    (**p).length = length;
}

// 9 9 9 (buffer with numbers stored in reverse [ex. 0 0 1 -> 100])
// 1
// 0 0 0 1 -> use a carry to store the second digit of each addition, if carry = 1

void plusplus(pyint *p)
{
    int carry = 1;
    int i = 0;
    while (carry < 1 && i < p->length)
    {
        int sum = p->buffer[i] + carry;
        p->buffer[i] = sum % 10;
        carry = sum / 10;
        i++;
    }
    //add another digit
    if (carry == 1)
    {
        p->buffer = (int *)realloc(p->buffer, (p->length + 1) * sizeof(int));
        p->buffer[p->length] = 1; //when adding 1, the leftover carry can only ever be one
        p->length++;
    }
}

void print_pyint(pyint *p)
{
    int i;
    for(i = p->length; i >= 0; i--)
    {
        printf("%d", p->buffer[i]);
    }
    printf("/n");
}