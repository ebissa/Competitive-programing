class Solution:
    def minimumIncompatibility(self, A: List[int], K: int) -> int:
        S = len(A) // K
        # pre-calc the bitmasks
        M = reduce(lambda M, i: {
                n | (1 << i) for i in range(len(A)) 
                for n in M if (n >> i) & 1 == 0 
                and all((n >> j) & 1 == 0 or A[j] != A[i] for j in range(len(A)))
            },
            range(S),
            {0}
        )

        # find 'incompatability' for each mask 
        D = {
            m: max(A[i] for i in range(len(A)) if (m >> i) & 1)\
                - min(A[i] for i in range(len(A)) if (m >> i) & 1)\
                for m in M
        }
        
        @cache
        def f(m: int) -> int:
            if m == (1 << len(A)) - 1: return 0
            return min(
                (f(m | nm) + D[nm] for nm in M if not (nm & m)), default=maxsize
            )

        return f(0) if f(0) < maxsize else -1
        