class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)
        if endWord not in wordList:
            return 0
        queue = deque([(beginWord, 1)])
        while queue:
            word, distance = queue.popleft()
            if word == endWord:
                return distance
            for i in range(len(word)):
                for ch in "abcdefghijklmnopqrstuvwxyz":
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in wordSet:
                        wordSet.remove(new_word)
                        queue.append((new_word, distance + 1))
        return 0
