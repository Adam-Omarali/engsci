#include <stdio.h>
#include <string.h>

int my_strcmp(char *str1, char *str2)
{
    if (strlen(str1) != strlen(str2))
    {
        return 0;
    }
    for (int i = 0; i <  strlen(str1); i++)
    {
        if(str1[i] != str2[i])
        {
            return 0;
        }
    }
    return 1;
}

int main()
{
    char str1[] = "abcd", str2[] = "xywz", str3[] = "abcd";
    printf("%d\n", my_strcmp(str1, str2));
    printf("%d\n", my_strcmp(str1, str3));
} 