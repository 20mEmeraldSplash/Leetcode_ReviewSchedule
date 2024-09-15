class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0

        queue = deque([(beginWord, 1)])
        wordLen = len(beginWord)

        while queue:
            currentWord, steps = queue.popleft()

            for i in range(wordLen):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    nextWord = currentWord[:i] + char + currentWord[i + 1:]

                    if nextWord == endWord:
                        return steps + 1

                    if nextWord in wordSet:
                        wordSet.remove(nextWord)  # 标记为已访问，防止重复遍历
                        queue.append((nextWord, steps + 1))
        return 0