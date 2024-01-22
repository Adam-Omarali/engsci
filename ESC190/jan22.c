#include <stdio.h>

int str_len(const char *s)
{
    int i = 0;
    //Typical way
    // while (s[i] != '\0')
    // {
    //     i++;
    // }
    i = 0;

    //Not best practice since hard to read
    while (*(s++)){ //*s == '\0' can be treated as a boolean
        i++;
    }
    return i;
}

int main()
{
    printf("%d\n", str_len("Hello"));
    return 0;
}