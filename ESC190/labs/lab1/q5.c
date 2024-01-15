#include <stdio.h>

int len(char *p_a)
{
    int i = 0;
    while (*(p_a + i) != '\0'){
        i++;
    }

    return i;
    //runtime complexity is the length of the string
}

int main()
{
    char *hi = "hello";
    // printf("%ld\n", &hi); //hi gives memory address where first char is stored, &hi gives memory address of hi
    printf("%d\n", len(hi));
    return 0;
}