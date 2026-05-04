class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        left = 0
        right = 0
        n = len(s)
        maxfreq = 0
        result = 0
        while right < n:
            if s[right] not in freq:
                freq[s[right]] = 1
            else:
                freq[s[right]] += 1
            if freq[s[right]] > maxfreq:
                maxfreq = freq[s[right]]
            dif = right - left + 1 - maxfreq
            if dif > k:
                freq[s[left]] -= 1
                left += 1

            result = max(result, right - left + 1)         
            right += 1   
        return result