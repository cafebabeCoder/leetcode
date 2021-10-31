/*
 * @lc app=leetcode.cn id=1855 lang=cpp
 *
 * [1855] 下标对中的最大距离
 */
#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int maxDistance(vector<int>& nums1, vector<int>& nums2) {
        int res = 0;
        for(int j=nums2.size()-1, i=nums1.size()-1; j>=0; j--){
            while(i && nums1[i-1]<=nums2[j]){  // i=0时不会越界
                i -= 1;
            }
            if(nums1[i] <= nums2[j]){
                res = max(res, j-i);
                // printf("j=%d i=%d res=%d\n", j, i, res);
            }
        }
        return res;
    }
};
// @lc code=end
int main(){
    Solution s;
    int n1[] = {2, 2, 1} ;//{30,29,19,5};
    int n2[] = {10, 10, 1}; //{25,25,25,25,25};
    vector<int> nums1(n1, n1+3);
    vector<int> nums2(n2, n2+3) ;
    int res = s.maxDistance(nums1, nums2);
    cout<<res;
}
