class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        freq1 = Counter(s1)
        lg = len(s1)
        freq2 = Counter(s2[:lg])
        if freq1 == freq2:
                return True
        for right in range(lg, len(s2)):
            left_char = s2[right - lg]
            freq2[left_char] -= 1
            if freq2[left_char] == 0:
                del freq2[left_char]

            freq2[s2[right]] += 1

            if freq1 == freq2:
                return True
        return False
            

