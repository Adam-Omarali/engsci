# include <stdio.h>
# include <stdlib.h>
# include <string.h>
# include "autocomplete.h"

//str and stream should have a size of 200 or less
int get_str_by_delimeter(char *str, char *stream, char delimeter, int start){
    int i = 0;
    while(stream[start] != delimeter && start <= 200){
        str[i] = stream[start];
        start++;
        i++;
    }
    str[i] = '\0';
    return i;
}

int cmpfunc(const void *a, const void *b){
    const term *t1 = a;
    const term *t2 = b;
    int i = 0;
    for(i = 0; t1->term[i] != '\0' || t2->term[i] != '\0'; i++){
        if (t1->term[i] < t2->term[i])
            return -1;
        else if (t1->term[i] > t2->term[i])
            return 1;
    }
    if (t1->term[i] == '\0')
        return -1;
    
    return 1;
}


void read_in_terms(struct term **terms, int *pnterms, char *filename){

    FILE *fp = fopen(filename, "r");
    if (fp == NULL)
    {
        printf("No file found");
        exit(1);
    }

    char c[200]; 
    double weight;
    int termCount = 0;
    int num_whitespaces = 5 + 1;
    while (fgets(c, sizeof(c), fp)){
        //get number of lines in the file
        if (c[0] != ' '){
            char *buffer = (char *)malloc(200);
            get_str_by_delimeter(buffer, c, '\n', 0);
            termCount = atoi(buffer);
            *pnterms = termCount;
            *terms = (term *)malloc(sizeof(term) * termCount);
            free(buffer);
        }
        else{
            char *buffer = (char *)malloc(200);
            //process weight and terms
            int num_digits = get_str_by_delimeter(buffer, c, '\t', num_whitespaces);
            weight = atof(buffer);
            (*terms)[*pnterms - termCount].weight = weight;
            get_str_by_delimeter((*terms)[*pnterms - termCount].term, c, '\n', num_whitespaces + num_digits + 1); //+1 for tab character
            termCount--;
            free(buffer);
        }
    }

    qsort(*terms, *pnterms, sizeof(term), cmpfunc);
    fclose(fp);
}


int lowest_match(struct term *terms, int nterms, char *substr){
    int left = 0;
    int right = nterms - 1;
    int mid = 0;

    while (left <= right){
        mid = (left + right)/2;
        int cmpr = strncmp(terms[mid].term, substr, strlen(substr));
        if (cmpr < 0){
            left = mid + 1;
        } 
        else if (cmpr > 0){
            right = mid - 1;
        }
        else{
            //at element
            while(mid > 0 && strncmp(terms[mid-1].term, substr, strlen(substr)) == 0){
                mid--;
            }
            return mid;
        }
    }
    return -1;
}

int highest_match(struct term *terms, int nterms, char *substr){
    int left = 0;
    int right = nterms - 1;
    int mid = 0;

    while (left <= right){
        mid = (left + right)/2;
        int cmpr = strncmp(terms[mid].term, substr, strlen(substr));
        if (cmpr < 0){
            left = mid + 1;
        } 
        else if (cmpr > 0){
            right = mid - 1;
        }
        else{
            //at element
            while(mid < nterms && strncmp(terms[mid+1].term, substr, strlen(substr)) == 0){
                mid++;
            }
            return mid;
        }
    }
    return -1;
}

int compare(const void *a, const void *b){
    const term *t1 = a;
    const term *t2 = b;
    return (int)(t2->weight - t1->weight);  
}


void autocomplete(struct term **answer, int *n_answer, struct term *terms, int nterms, char *substr){
    int start_ans = lowest_match(terms, nterms, substr);
    int end_ans = highest_match(terms, nterms, substr);
    *n_answer = end_ans - start_ans + 1;
    *answer = (term *)malloc(sizeof(term) * (*n_answer));
    for(int i = 0; i < *n_answer; i++){
        strcpy((*answer)[i].term, terms[start_ans + i].term);
        (*answer)[i].weight = terms[start_ans + i].weight;
    } 
    // for(int i = 0; i <= (*n_answer); i++){
    //     printf("%s, %f\n", (*answer)[i].term, (*answer)[i].weight);
    // }
    qsort(*answer, *n_answer, sizeof(term), compare);
}