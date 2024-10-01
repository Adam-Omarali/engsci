/*
Problem 2 -- 20 pts (8 of 20 autograded)
========================================

  Write a C program that takes in an array of strings and the number of strings in the array, and 
  returns 1 if there are repetitions in the array, and 0 otherwise.
 
  The function *must* run in average O(n) time, where n is the number of strings and must use hashing.
  The function siganture must be:

  int repeats(char **strs, int strs_sz);

  Briefly justify why the function runs in O(n) overage time in the comments.
*/


/*
create a map from strings to numbers, say the numbers being mapped to will be in the range 0~5 inclusive (I pulled the number 5 out of thin air). 
You can create a container of 6 numbers and initialize them to some "empty initial state" representing "has not seen the string", e.g. container = [-1,-1,-1,-1,-1,-1]. 

When going through the strings, perform the map. For each string, say map(string)=i. We then change container[i] to 1. 
Now later down the road, if we see a container[i]=1 instead of -1 for another string, then we know a previous string has mapped to i already. 
If our map is one-to-one, then this must mean we have seen the current string previously!

For collisions, i.e. two strings mapping to the same number, simply check in that subset. 
On average, collision probability is small compared to size of list.
e.g. if hash is done via modulo 100, then collision rate is only 1%. 

Note: accessing an array element (i.e. container[i]) is O(1).
Also note: sorting would not work: no comparison-based sorting algorithms can achieve linear time
*/

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int hash_for(char *s){
   // the hash I use: add up all the characters in the string as numbers, then modulo 100
   int num = 0;
   for (int i=0; i<strlen(s); i++){
      num += (s[i] - '0');    // convert a char to a number 
   }
   return num % 100;
}

// I will also demonstrate how to loop through a string if you can't use strlen() for some reason
int hash_while(char *s){
   int num = 0;
   char *cur = s;
   while (*cur != '\0'){
      num += (*cur - '0');    
      cur++;
   }
   return num % 100;
}


int repeats(char **strs, int strs_sz){
    // 1. 
    // If you don't want to consider collisions, then a simple container is enough. 
    // Create the container. We used modulo 100 so container should have 100 slots
    // use 0 to represent "has not seen a string that maps to this number"
    // i.e. elements represent the number of strings that map to this slot
    int *hashResult = calloc(100*sizeof(int), sizeof(int));

    // If you want to consider collisions, 
    // for each slot, also create an array for all possible strings that could map to this slot
    // maximum size of this array is the number of strings in the original array;
    // need to create 100 such arrays, so need an array of 100 arrays of strings
    // an element of this container is "an array of strings", or a char**
    // so this container itself is char***
    char ***s = malloc(100*sizeof(char**));
    for (int j=0; j<100; j++){
       s[j] = malloc(strs_sz*sizeof(char*));  //malloc each char**
    }

    // 2. go through the strings, add them to the container's corresponding index
    for (int i=0; i<strs_sz; i++){
       int index = hash_for(strs[i]);
       //printf("%d\n", index);
       s[index][hashResult[index]] = strs[i];
       hashResult[index] += 1;
    }

/*
    // uncomment this loop to see what hashResult and s actually represents!
    for (int p=0; p<100; p++){
      if (hashResult[p] != 0) {
         printf("%d, %d, hr\n", p, hashResult[p]);
         for (int j=0; j<hashResult[p]; j++){
            printf("%s\n", s[p][j]);
         }
      }
    }
*/

    // 3. check for duplicates
    for (int p=0; p<100; p++){
      if (hashResult[p] >= 2){
         // if a slot has more than 2 strings mapped to it, need to check among this small subset for duplicates
         // double loop in here is fine: the collision subset is small enough compared to the original list
         // notice the question asks for 0(n) AVERAGE time, not worst time
         for (int j=0; j<hashResult[p]; j++){
            for (int k=0; k<hashResult[p]; k++){
               if ((strcmp(s[p][j], s[p][k])==0) && (j!=k)){// same strings 
                  return 1;
               }
            }
         }
      }
    }

    return 0;
}

int main(){
  char *strs[] = {"ESC", "PHY", "MSE", "CIV"};
  printf("%d\n", repeats(strs, 4)); // 0

  char *strs1[] = {"ESC", "PHY", "MSE", "CIV", "CVI"};
  printf("%d\n", repeats(strs1, 5)); // 0

  char *strs2[] = {"ESC", "PHY", "MSE", "CIV", "ESC"};
  printf("%d\n", repeats(strs2, 5)); // 1
}



/*Marking scheme:
6 max points for a non O(n^2) solution  (remove autograder points if necessary)

Out of the 12 manual points:
9 points for using hashing, but in a flawed way (e.g., not considering the possibility of two strings hashing to the same slot)
12 points for everything correct or almost correct.
*/