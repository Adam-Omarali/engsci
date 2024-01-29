#include <stdio.h>
#include <stdlib.h>

void print_txt(char *filename, int N)
{
    // char **lines;
    char line[200];
    FILE *fp = fopen(filename, "r");


    if (fp == NULL)
    {
        printf("null\n");
    }
    else
    {
        for(int i = 0; i < N; i++){
            fgets(line, sizeof(line), fp); //read in at most sizeof(line) characters
            printf("%s\n", line);
            //(including ’\0’) into line.
        }
        fclose(fp);
    }
}

void avg_int(char *filename)
{
    char line[200];
    FILE *fp = fopen(filename, "r");

    int count = 0;
    int sum = 0;

    if (fp == NULL)
    {
        printf("null\n");
    }
    else
    {
        while(fgets(line, sizeof(line), fp)) {
            count++;
            sum += atoi(line);
        }
    }
    printf("%f\n", (double)sum / count);
}

int main()
{
    char *filename = "test.txt"; //make sure the build folder is at same directory level as txt
    int N = 1;
    print_txt(filename, N);

    avg_int("average.txt");
}