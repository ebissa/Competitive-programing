class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l = max_ = 0
        tree = defaultdict(int)
        for r in range(len(fruits)):
            tree[fruits[r]] += 1
            while len(tree) > 2:
                tree[fruits[l]] -= 1
                if not tree[fruits[l]]:
                    del tree[fruits[l]]
                l += 1
            max_ = max(max_, sum(tree.values()))
        return max_