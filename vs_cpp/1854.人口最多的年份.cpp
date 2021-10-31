/*
 * @lc app=leetcode.cn id=1854 lang=cpp
 *
 * [1854] 人口最多的年份
 */
#include<iostream>
#include<vector>
using namespace std;

// @lc code=start
class Solution {
public:
    int maximumPopulation(vector<vector<int> >& logs) {
        int res = 0;
        int start = 0;
        for(int i=1950; i<=2050; i++){
            int s = 0;
            for (int j=0; j<logs.size(); j++){
                vector<int> log = logs[j];
                if(log[0]<=i && log[1]>i){
                    s += 1;                    
                }
                if(s > res)
                {
                    res = s;
                    start = i;
                }

            }
        }
        return start;
    }
};
// @lc code=end
int main(){
    Solution s;
    vector<int> t(2, 5);
    vector<vector<int> > v;
    v.push_back(t);
    int i = s.maximumPopulation(v);
    cout<<i<<endl;
    return 0;
}
