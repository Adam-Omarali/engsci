#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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

void change_name(student2 s)
{
    s.name = (char *)malloc(sizeof(char) * 10);
    strcpy(s.name, "Bob");
}

void change_name_wptr(student2 *s)
{
    (*s).name = "Not Adam";
}

int main()
{
    //q7
    student2 *s; //have to declare as *s, not s[10] sinze &s will go to the first student and get its address
    create_block2(&s, 10);

    //q8
    set_name2(&s[0], "Bob");
    printf("%s\n", s[0].name);

    //q9
    destroy_block2(s, 10);
    printf("%s\n", s[0].name);

    //q10
    student2 s2 = {"Adam", "10101", 2027};
    change_name(s2);
    printf("%s\n", s2.name);

    change_name_wptr(&s2);
    printf("%s\n", s2.name);

}