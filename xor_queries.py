class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        cur_xor = 0
        prexor = {-1:0}
        res = []
        for i in range(len(arr)):
            cur_xor ^= arr[i]
            prexor[i] = cur_xor    
        for q in queries:
            start, end = q
            res.append(prexor[end]^prexor[start-1])
        return res
