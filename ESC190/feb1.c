#include <stdlib.h>
#include <stdio.h>
#include <string.h>

typedef struct student1 {
    char name[50];
    double gpa;
} student1;

//store pointer to name inside the struct
//student2 takes up less space because storing char * takes up less space than name[50]
typedef struct student2 {
    char *name;
    double gpa;
} student2;

student1* test()
{
    student1 s1[150];
    return s1;
}

int main()
{
    student1 s1[150]; //will crash if you return 
    
    printf("%ld\n", test());

    student1 *s1_block = (student1 *)malloc(sizeof(student1) * 150);
    //fine if you return because the address is valid until we explicitly free

    student2 s2[150]; 
    //s2[0].name will print some arbitrary value
    //can print s2[0].gpa
    printf("%s\n", s2[0].name);
    printf("%f\n", s2[0].gpa);

    s2[0].name = "John"; //but not allowed to modify s2[0].name[x] after
    //or
    s2[1].name = (char *)malloc(sizeof(char) * 4);
    strcpy(s2[1].name, "John");

    //make a block of pointers to student2
    student2 **p_s2_block; //the address of the first element of the block of objects that are of type student2 *
    p_s2_block = (student2 **)malloc(sizeof(student2 *) * 150); //150 empty cells where addresses can be stored which each point to a student2 *

    int i;
    for (int i = 0; i < 150; i++)
    {
        p_s2_block[i] = (student2 *)malloc(sizeof(student2)); //give enough space to store a singular student2
        p_s2_block[i]->gpa = 4.0; //-> says here is an address of a student and go get his gpa; syntatic sugar for (*p_s2_block[i]).gpa

        p_s2_block[i]->name = (char *)malloc(sizeof(char *) * 5);
    }
}