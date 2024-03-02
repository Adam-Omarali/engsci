#include <stdio.h>
#include <stdlib.h>

char * strcat_rec(char *dest, const char *src)
{
    if (*src == '\0'){
        return dest;
    }

    int i = 0;
    while (*(dest+i) != '\0'){
        i++;
    }
    *(dest + i) = *src;
    *(dest + 1 + i) = '\0';
    strcat_rec(dest, src+1);
    return dest;
}

int main()
{
    char * dest = (char *)malloc(7);
    dest[0] = 'E';
    dest[1] = 'S';
    dest[2] = 'C';
    char * src = "190";
    printf("%s\n", strcat_rec(dest, src));
}