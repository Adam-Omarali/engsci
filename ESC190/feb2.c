#include <string.h>
#include <stdlib.h>
#include <stdio.h>

void safer_str_cat(char **p_str1, char *str2)
{
    //Need enough space at *str1 to hold both str1 and str2

    //Amount of space = strlen(str1) + strlen(str2) + 1
    int space = strlen(*p_str1) + strlen(str2) + 1;
    *p_str1 = (char *)realloc(*p_str1, sizeof(char) * space); //since sizeof(char) = 1 always, no need to specify sizeof(char)

    if(*p_str1 == NULL)
    {
        printf("Safer strcat failed to allocate memory\n");
        exit(1);
    }

    strcat(*p_str1, str2);

}

int main()
{
    char *str1 = (char *)malloc(sizeof(char) * 10);
    str1 = "Eng";

    char *str2 = "Sci";
    safer_str_cat(&str1, str2);
}