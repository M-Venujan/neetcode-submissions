class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low , high = 1 , max(piles)
        min_k = max(piles)
        while high >= low:
            mid = (low + high) // 2
            mid_number = mid
            hours = 0
            for i in piles:
                if i % mid_number == 0:
                   hours += (i // mid_number)

                else:
                    hours += (i// mid_number) + 1
            
            if hours <= h:
                min_k = min(min_k , mid_number)
                high = mid - 1
            elif hours > h:
                low = mid + 1
        return min_k


