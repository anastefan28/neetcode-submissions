class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0
        n = len(s)
        maxlen = 0
        currlen = 0
        lastseen = {}
        while right < n:
            if s[right] not in lastseen or lastseen[s[right]] < left:
                currlen += 1
            else:
                left = lastseen[s[right]] + 1
                maxlen = max(maxlen, currlen)
                currlen = right - left + 1
            lastseen[s[right]] = right
            right += 1
        maxlen = max(maxlen, currlen)
        return maxlen
