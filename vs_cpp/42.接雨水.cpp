/*
 * @lc app=leetcode.cn id=42 lang=cpp
 *
 * [42] 接雨水
 */
#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int trap(vector<int>& height) {
        int n=height.size();
        if(n == 0) return 0;
        int max_l = height[0];
        int max_r = height[n-1];
        int l =0, r=n-1;
        long long res = 0;
        while(l <= r){
            max_l = max(max_l, height[l]);
            max_r = max(max_r, height[r]);
            // printf("l=%d, r=%d", l, r);
            if (max_l < max_r){
                res += max_l - height[l];
                l += 1;
            }
            else{
                res += max_r - height[r];
                r-=1;
            }
        }
        return res;
    }
};
// @lc code=end

int main(){
    Solution s;
    int n1[] = {0,1,0,2,1,0,1,3,2,1,2,1};
    vector<int> nums1(n1, n1+12);
    s.trap(nums1);
}