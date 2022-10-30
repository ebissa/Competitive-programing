class Solution(object):
    def topKFrequent(self, nums, k):
        d={}
        res=[]
        for n in nums:
                d[n]=1+ d.get(n,0)
        lists=sorted(d.items(),key=lambda freq:freq[1])
        for i in range((k)):
            res.append(lists.pop()[0])
        return res
            
