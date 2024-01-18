## Interpreted vs Compiled Languages

Python is an interpreted language, meaning writing python file.py runs a script itself that executes code block by block

Machine Code $\rightarrow$ Moving and writing data to memory addresses

A compiler takes hunan-readable code and translates it to machine code.
The lower level language, the easiar it is to translate into machine code. The less abstraction it has. Ex - For loops and functions are an abstraction.

C for loops include more detail to make it less abstract

Typical workflow for high level CS:
- Write in Python
- Figure out the ineffecient part of the program
- Write that part in C

## To run c
```bash
gcc -o build/jan18 jan18.c -lm
./build/jan18
```
gcc: The compiler that converts c code to an executable
-o path/filename: Specify the name of executable file and where you want it to live
jan18.c: The c file to compile
-lm: Linker option (links the math library)


## Memory
An 8Gb computer has $8*10^9$ bytes (aka, memory addresses).

When you have a lot of tabs, all the computer's fast memory is taken up, and it has to store data on the hard drive. 
- What is fast memory?
- Addresses like 45 (if pass in int a = 45, rather than &a) are not in this fast memory

#### Storing Values
Values of type string and array are stores as blocks of value in memory.

Different types of values take different amounts of storage:
- Integers take 4 memory address (starting address + 4)
- Chars take up one?

#### Pointer Arithmetic

int array = {3, 4};
*(arr + 1) -> pointer arithmetic knows the elements are of type int and will change this is *(arr + 4), so the +x is essentially the xth element in the array

