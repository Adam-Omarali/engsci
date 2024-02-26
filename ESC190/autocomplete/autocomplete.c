# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include "autocomplete.h"

void store_str_to_delimeter(char *string, char *stream, char delimeter, int start){
    int i = 0;

    //start must be <200 so i does not go out of bounds when adding the null character
    while(start < 200 && stream[start] != delimeter){
        string[i] = stream[start];
        i++;
        start++;
    }

    string[i] = '\0';
}

int get_whitespaces(char *string){
    int i = 0;
    while (string[i] == ' '){
        i++;
    }
    return i;

}

int compare_term(const void *a, const void *b){
    const term *t1 = a;
    const term *t2 = b;
    return strcmp(t1->term, t2 ->term);
}


void read_in_terms(struct term **terms, int *pnterms, char *filename){

    FILE *fp = fopen(filename, "r");
    if (fp == NULL)
    {
        printf("no file");
        exit(1);
    }

    char c[200]; 
    int termCount = 0;
    char *buffer = (char *)malloc(200);
    while (fgets(c, sizeof(c), fp)){
        //get number of lines in the file
        if (c[0] != ' '){
            store_str_to_delimeter(buffer, c, '\n', 0);
            termCount = atoi(buffer);
            *pnterms = termCount;
            *terms = (term *)malloc(sizeof(term) * termCount);
        }
        else{
            //process weight and terms
            store_str_to_delimeter(buffer, c, '\t', get_whitespaces(c));
            (*terms)[*pnterms - termCount].weight = atof(buffer);
            store_str_to_delimeter((*terms)[*pnterms - termCount].term, c, '\n', get_whitespaces(c) + strlen(buffer) + 1); //+1 for tab character
            termCount--;
        }
    }

    free(buffer);

    qsort(*terms, *pnterms, sizeof(term), compare_term);
    fclose(fp);
}

int lowest_match(struct term *terms, int nterms, char *substr){
    int left = 0, right = nterms - 1;
    int len = strlen(substr);
    while (left <= right){
        int mid = (right + left) / 2;
        if (strncmp((terms+mid)->term, substr, len) < 0){
            left = mid + 1;
        }
        else if (strncmp((terms+mid)->term, substr, len) > 0){
            right = mid - 1;
        }
        else if (strncmp((terms+mid)->term, substr, len) == 0 && mid == 0){
            return mid;
        }
        else if (strncmp((terms+mid)->term, substr, len) == 0 && strncmp((terms+mid-1)->term, substr, len) < 0 ){
            return mid;
        }
        else{
            right = mid - 1;
        } 
    }
    return -1; 
}

int highest_match(struct term *terms, int nterms, char *substr){
    int left = 0, right = nterms - 1;
    int len = strlen(substr);
    while (left <= right){
        int mid = (right + left) / 2;
        if (strncmp((terms+mid)->term, substr, len) < 0){
            left = mid + 1;
        }
        else if (strncmp((terms+mid)->term, substr, len) > 0){
            right = mid - 1;
        }
        else if (strncmp((terms+mid)->term, substr, len) == 0 && mid == nterms - 1){
            return mid;
        }
        else if (strncmp((terms+mid)->term, substr, len) == 0 && strncmp((terms+mid+1)->term, substr, len) > 0){
            return mid;
        }
        else{
            left = mid + 1;
        } 
    }
    return -1; 
}

int compare_weight(const void *a, const void *b){
    const term *t1 = a;
    const term *t2 = b;
    return (int)(t2->weight - t1->weight);  
}

void autocomplete(struct term **answer, int *n_answer, struct term *terms, int nterms, char *substr){
    int low = lowest_match(terms, nterms, substr);
    int high = highest_match(terms, nterms, substr);
    *n_answer = high - low + 1;
    *answer = (term *)malloc(sizeof(term) * (*n_answer));

    for(int i = 0; i < *n_answer; i++){
        strcpy((*answer)[i].term, terms[low + i].term);
        (*answer)[i].weight = terms[low + i].weight;
    } 
    qsort(*answer, *n_answer, sizeof(term), compare_weight);
}