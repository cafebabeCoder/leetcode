/*
 * @lc app=leetcode.cn id=496 lang=cpp
 *
 * [496] 下一个更大元素 I
 */
#include<iostream>
#include<vector>
#include<stdio.h>
#include<tr1/unordered_map>
using namespace std;
using namespace std::tr1;

// @lc code=start
class Solution {
public:
    vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {

       int n1 = nums1.size();
       int n2 = nums2.size();
       unordered_map<int, int> num_map;

       stack<int> s;
       for(int i=n2-1; i>=0; i--){
           while(!s.empty() && s.top()<=nums2[i])
            s.pop(); 
           num_map[nums2[i]] = s.empty()? -1:s.top();
           s.push(nums2[i]);
       }

    //    for(auto& v:num_map)
    //     cout<<v.first<<" : "<<v.second<<endl;
       vector<int> res(n1);       
       for(int i=0; i<n1; i++){
           if(num_map.find(nums1[i])!=num_map.end()) res[i]=num_map[nums1[i]]; else res[i]=-1;
       }
       return res;
    }
};
// @lc code=end
