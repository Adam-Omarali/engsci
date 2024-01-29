#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include "student1.h"

typedef struct student2{
    char *name;
    char *student_number;
    int year;
} student2;

void create_block2(student2 **p_p_s, int num_students)
{
    *(p_p_s) = (student2 *)malloc(sizeof(student2) * num_students);
    for (int i = 0; i < num_students; i++)
    {
        (*p_p_s)[i].name = 0;
        (*p_p_s)[i].student_number = 0;
    }
}

void set_name2(student2 *s, char *name)
{
    (*s).name = (char *)malloc(sizeof(char) * (strlen(name) + 1));
    strcpy((*s).name, name);
}

void destroy_block2(student2 *s, int num_students)
{
    for(int i = 0; i < num_students; i++)
    {
        //do we have to check if name exists
        free(s[i].name);
        s[i].name = NULL;
    }
    free(s);
}

void print_student(student1 s)
{
    printf("%s\n", s.name);
    printf("%s\n", s.student_number);
    printf("%d\n", s.year);
}

void set_default_name(student1 *p_s)
{
    strcpy((*p_s).name,  "Default Student"); 
    (*p_s).year = 5;
    print_student(*p_s);
}

void set_default_name_wrong(student1 s)
{
    strcpy(s.name,  "Default Student"); //will make a copy of student
    s.year = 5; //this will also edit the local copy of student
    print_student(s); //will print correctly inside function since local copy, but not outside function

}

void create_block1(student1 **p_p_s, int n_students)
{
    //previously had p_p_s -> this would just change the local p_p_s
    *p_p_s = (student1 *)malloc(sizeof(student1) * n_students); //student * == array of students
}

void set_name(student1 *s, char *name)
{
    int bound = strlen(name);
    if (bound > 199)
    {
        bound = 199;
    }
    for (int i = 0; i < 199; i++)
    {
        (*s).name[i] = name[i];
    }
}

void destroy_bloc1(student1 **s)
{
    free(*s); //this only says the memory is writable, but it doesn't actually remove the memory
    *s = NULL; //set to null to not use the memory in the rest of the program
}

int main()
{

    //q2
    student1 s1;
    strcpy(s1.name, "Bob");
    strcpy(s1.student_number, "1234567890");
    s1.year = 2;

    print_student(s1);

    //q3
    set_default_name(&s1);
    print_student(s1);



    strcpy(s1.name, "Bob");
    s1.year = 2;

    set_default_name_wrong(s1);
    print_student(s1);

    //q4
    student1 *students;
    create_block1(&students, 20);


    set_name(&students[0], "Adam");
    printf("%s\n", students[0].name);

    char out_of_bounds[200]; //declaring this as char *out_of_bounds would result in seg fault since doesn't know how much memory to set aside
    for (int i = 0; i < 201; i++)
    {
        out_of_bounds[i] = 'h';
    }

    set_name(&students[1], out_of_bounds);
    printf("%s\n", students[1].name);

    //q6
    destroy_bloc1(&students); //pass in address of students to set the array to null, otherwise just setting local array to null
    printf("%s\n", students[1].name); //should seg fault!

}