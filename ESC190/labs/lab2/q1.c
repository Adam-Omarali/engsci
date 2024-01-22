#include <stdio.h>
#include <stdlib.h>

void takeStr(char **p_c, int * p_add) //address of a pointer to char, address of an iont
{
    int strlen;
    scanf("%d\n", &strlen);
    strlen++;
    *p_c = (char *)malloc(sizeof(char) * strlen);
    *p_add = strlen;
    for (int i = 0; i < strlen - 1; i++)
    {
        char c;
        scanf("\n%c", &c); //put /n before
        *(*(p_c)+i) = c; //go and get the pointer value of the first letter, then move to the next pointer, **(p_c+i) would try and go get the address after the first address
    }
    *(*(p_c) + strlen) = '\0';


}

int main()
{
    char * userStr;
    int strlen;
    takeStr(&userStr, &strlen);
    printf("Size of char + null: %d\n", strlen);
    //print char
    // while(*userStr)
    // {
    //     printf("%c\n", *userStr);
    //     userStr++;
    // }
    printf("%s\n", userStr);
    free(userStr);
    return 0;
}