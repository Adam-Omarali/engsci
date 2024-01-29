#include <stdio.h>
#include "jan29.h" //paste the code from the header file here
#include <stdlib.h>
#include <string.h>

#if !defined(ESC190) //check if ESC190 was defined in jan29.h
#define ESC190 

typedef struct course{
    int code;
} course;

#endif

typedef struct student {
    char* name;
} student;

typedef struct studen_wptr {
    char* name;
} student_wptr;

int main()
{
    p();

    char *name;
    name = (char *)malloc(sizeof(char) * 10);
    // name = "MAT185"; //if didn't free name, this will be a memory leak
    strcpy(name, "ESC190");
    name[4] = '8'; //okay
    printf("%s\n", name);

    char *name2 = (char *)malloc(sizeof(char) * 10);
    name2 = "MAT185"; //if didn't free name, this will be a memory leak
    name2[4] = '8'; //not okay, since name is a string literal, it is stored in read-only memory as a const char, see this a bus error
    printf("%s\n", name2);

    char name3[200] = "Bob";
    //name3 = "Alice"; //bad, can't assign to the array, can change the elements though


    student s1;
    s1.name = "Bob";

    student_wptr s2;
    strcpy(s2.name, "Alice"); //bad, s2.name is not pointing to anything, so strcpy will seg fault
    s2.name = "Alice"; //okay, saying take the address where string literal "Alice" is stored, and assign that address to s2.name

    return 0;
}