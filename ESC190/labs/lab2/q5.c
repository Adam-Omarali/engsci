#include <stdio.h>
#include <string.h>
#include <ctype.h>

int my_atoi(char *str)
{
    int ret;
    for (int i = 0; i < strlen(str); i++)
    {
        if(isdigit(str[i]))
        {
            int num = (int)str[i] - '0';
            ret = ret * 10 + num;
        }
        else
        {
            return 0;
        }
    }
    return ret;
}

int main()
{
    char *str = "789";
    printf("%d\n", my_atoi(str));
}