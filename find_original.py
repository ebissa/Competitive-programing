class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
      if len(changed)%2:
        return []

      changed.sort()
      c, res = Counter(changed), []
	  
      for n in changed:
        if 2*n in c and c[n] > 0:
          c[n] -= 1
          if c[2*n] > 0:
            c[2*n] -= 1
            res.append(n)
		  
          else:
            c[n] += 1
       
      if len(res) == len(changed)/2:
        return res
      
      
      return []
