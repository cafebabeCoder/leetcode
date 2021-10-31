/*
 * @lc app=leetcode.cn id=1859 lang=cpp
 *
 * [1859] 将句子排序
 */
#include<iostream>
#include<vector>
#include<stdio.h>
using namespace std;

// @lc code=start
class Solution {
public:
    string sortSentence(string s) {
        unsigned int len = s.size();
        unordered_map<int, int> num_map;
        unsigned int i = 0;
        vector<string> tmp;  // 临时存tmp
        unsigned idx = 0;
        for(i=len; i >=0; i--){
            if(i == len-1 || s[i+1] == ' '){
                string s1{s[i]};
                cout<< s1<<endl;
                // idx = std::atoi(s1);
            }
            else if(s[i] ==' '){
                num_map[idx] = 0;
                idx = 0;
                tmp.clear();
            } 
            else{}
            // tmp.push(s[i])
        }
    }
};
// @lc code=end

