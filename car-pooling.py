class Solution(object):
    def carPooling(self, trips, capacity):
        trips.sort(key=lambda t: t[2])
        last=trips[-1][2]
        passchange=[0]*(last+1)
        for t in trips:
            cap,start,end=t
            passchange[start]+=cap
            passchange[end]-=cap
        cur_pass=0
        for i in range(last+1):
            cur_pass+=passchange[i]
            if cur_pass>capacity:
                return False
        return True
