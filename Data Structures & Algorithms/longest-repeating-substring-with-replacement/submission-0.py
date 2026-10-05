class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        window_size = 0
        max_freq = 0
        max_length = 0
        count = defaultdict(int)

        for right in range(len(s)):
            window_size += 1
            count[s[right]] += 1
            max_freq = max(max_freq , count[s[right]])
            while window_size - max_freq > k:
                count[s[left]] -= 1
                left += 1
                window_size -= 1
            max_length = max(max_length , window_size)
        return max_length

                    


