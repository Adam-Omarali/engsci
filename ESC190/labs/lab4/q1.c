#include <stdio.h>

int main()
{
    // int a = 43;
    // int *p_a = a;
    // printf("%ld", *p_a);

    FILE *fp = fopen("test.txt", "r");
    // if (fp == NULL)
    // {
    //     pritnf("No file\n");
    // }

    fclose(fp);
}