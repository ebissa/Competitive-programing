chalks = k
        i = 0
        n = len(chalk)
        if n == 1:
            return 0
        prefix = sum(chalk)
        k = k % prefix
        for i in range(n):
            if chalk[i] > k:
                return i
            k -= chalk[i]       


