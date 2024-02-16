#include "pyint.h"

int main()
{
    //* is the derefence operator
    pyint *p = 0;
    create_pyint(&p, 1);
    print_pyint(p);

}