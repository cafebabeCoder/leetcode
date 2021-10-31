/*
 * @lc app=leetcode.cn id=84 lang=cpp
 *
 * [84] 柱状图中最大的矩形
 */
#include<iostream>
// #include<stack>
#include<vector>
#include<stdio.h>
using namespace std;

// @lc code=start
class Solution {
public:
    int largestRectangleArea(vector<int>& heights) {
        int n = heights.size();
        vector<int> left(n), right(n);

        stack<int> s;
        for(int i =0; i<n; ++i){
            while(!s.empty() && (heights[s.top()] >= heights[i])){
                s.pop();
            }
            left[i] = s.empty() ? -1:s.top();
            s.push(i);
        }
        s = stack<int>();
        for(int i=n-1; i>=0; --i){
            while(!s.empty() && (heights[s.top()] >= heights[i])){
                s.pop();
            }
            right[i] = s.empty() ? n :s.top();
            s.push(i);
        }

        // for(int i=0; i<n;i++)
        //     printf("%d ", left[i]);
        // printf("\n");
        // for(int i=0; i<n; i++)
        //     printf("%d ", right[i]);
        int res= 0;
        for(int i=0;i<n;i++){
            res = max(res, (right[i]-left[i] - 1) * heights[i]);
        }
        return res;
    }
};
// @lc code=end

