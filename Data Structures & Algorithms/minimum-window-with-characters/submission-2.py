class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq1 = Counter(t)
        freq2 = Counter()
        left = 0
        have = 0
        need = len(freq1)
        min_lg = float("inf")
        result = ""
        for (right,ch) in enumerate(s):
            freq2[ch] += 1
            if ch in freq1 and freq2[ch] == freq1[ch]:
                have += 1
            while have == need:
                current_lg = right - left + 1
                if current_lg < min_lg:
                    min_lg = current_lg
                    result = s[left:right + 1]
                left_char = s[left]
                freq2[left_char] -= 1
                if left_char in freq1 and freq2[left_char] < freq1[left_char]:
                    have -= 1
                left += 1
        return result
                
                