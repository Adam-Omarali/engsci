typedef struct pyint {
    int *buffer;
    int length;

} pyint;

void create_pyint(pyint **p, int length);
void plusplus(pyint *p);
void print_pyint(pyint *p);