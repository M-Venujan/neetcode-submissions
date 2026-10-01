class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        count = defaultdict(int)
        max_string_len = 0
        for right in range(len(s)):
            count[s[right]] += 1
            while count[s[right]] > 1:
                count[s[left]] -= 1
                left += 1
            curr_str_len = right - left + 1
            max_string_len = max(max_string_len , curr_str_len)
        return max_string_len

