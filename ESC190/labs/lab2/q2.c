#include <stdio.h>
#include <string.h>

void strcat1(char *str1, char*str2)
{
    //resultant str stored in str1
    char *temp_str = str1;
    int size_str1 = strlen(str1);
    int size_str2 = strlen(str2);
    // str1 = (char *)malloc((size_str1 + size_str2) * sizeof(char));
    for (int i = 0; i < size_str1; i++)
    {
        str1[i] = temp_str[i];
    }
    for (int i = 0; i < size_str2; i++)
    {
        str1[i + size_str1] = str2[i];
    }
}

void strcat2(char *str1, char*str2)
{
    char *temp_str = str1;
    int size_str1 = strlen(str1);
    int size_str2 = strlen(str2);
    
    int i = 0;
    while (*(str1 + i))
    {
        *(str1 + i) = *(temp_str + i);
    }
    i = 0;
    while(*(str2 + i))
    {
        *(str1 + size_str1 + i) = *(str2 + i);
    }
}

int main()
{
    char str1[100] = "This is ", str2[] = "cool";
    //but what if str1 is not enough length
    strcat1(str1, str2);
    printf("%s\n", str1);
    char str3[100] = "This is ", str4[] = "cool";
    strcat1(str3, str4);
    printf("%s\n", str3);
    return 0;
}