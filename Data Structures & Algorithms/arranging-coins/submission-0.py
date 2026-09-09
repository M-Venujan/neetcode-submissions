class Solution:
    def arrangeCoins(self, n: int) -> int:
        l , r = 1 , n
        row = n
        while l <= r:
            m = (l + r) // 2
            needed_coins = (m*(m+1))/2
            if needed_coins > n:
                r = m - 1
            elif needed_coins < n:
                l = m + 1
                row = m
            else:
                return row
        return row
