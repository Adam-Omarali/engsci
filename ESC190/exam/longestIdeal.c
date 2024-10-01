#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

int longestIdealString(char* s, int k) {
    int l = (int) strlen(s);
    int lengths[26];
    int explored[26];
    int ret = 1;
    for (int i = 0; i < 26; i++)
    {
        lengths[i] = 1;
        explored[i] = 0;
    }
    explored[s[0] - 'a'] = 1;
    for (int i = 1; i < l; i++)
    {
        int max_subproblem = 0;
        for (int j = 0; j < 26; j++)
        {
            if(explored[j] == 0) continue; 
            if (abs(j + 'a' - s[i]) <= k)
            {
                if(lengths[j] > max_subproblem) max_subproblem = lengths[j];
            }
        }
        lengths[s[i] - 'a'] = max_subproblem + 1;
        if (lengths[s[i] - 'a'] > ret) ret = lengths[s[i]-'a'];
        explored[s[i] - 'a'] = 1;
    }
    return ret;
}

int main()
{
    printf("%d\n", longestIdealString("pvjcci", 4));
    return 0;
}
