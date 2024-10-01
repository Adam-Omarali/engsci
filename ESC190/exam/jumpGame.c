#include <stdbool.h>
#include <stdio.h>

bool canJump(int* nums, int numsSize) {
    //can reach an index i if the element at index j satisfies j + element[j] >= i
    if (numsSize == 1) return true;
    bool dp[numsSize - 1];
    for (int i = 0; i < numsSize - 1; i++)
    {
        dp[i] = false;
    }
    int target = numsSize - 1;
    //start at second last element
    for (int i = target - 1; i >= 0; i--)
    {
        if ((nums[i] + i) >= target)
        {
            dp[i] = true;
            target = i;
        }
    }
    return dp[0];
}