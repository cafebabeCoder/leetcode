class Solution(object):
    def permutation(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.res = []
        self.visit = {}
        for i in range(len(s)):
            self.visit[i] = False
        track = []
        ss = sorted(list(s))
       # print(ss)
        self.back_track(ss, track)
        print(self.res)

        return self.res

    def back_track(self, s, track):
        if len(s) == len(track) :
            #print(track)
            self.res.append("".join(track))
        
        for i in range(len(s)):
            if (self.visit[i]) or ((i >0) and not self.visit[i-1] and s[i-1] ==s[i]):
                continue
            self.visit[i] = True
            track.append(s[i])
            self.back_track(s, track)
            self.visit[i] = False
            track.pop()

s = Solution()
s.permutation("aabc")	 