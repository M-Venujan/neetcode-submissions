class Solution:
    def arrangeCoins(self, n: int) -> int:
        l , r = 1 , n
        row = 0
        while l <= r:
            m = (l + r) // 2
            needed_coins = (m*(m+1))/2
            if needed_coins > n:
                r = m - 1
            else:
                l = m + 1
                row = max(m , row)
        return row
