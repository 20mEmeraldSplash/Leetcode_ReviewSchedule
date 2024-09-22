class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        # 'abcdefghijklmnopqrstuvwxyz'
        wordList = set(wordList)
        if endWord not in wordList:
            return 0

        queue = deque([[beginWord, 1]])
        
        chars = 'abcdefghijklmnopqrstuvwxyz'
        
        while queue:
            currentWord, steps = queue.popleft()
            for i in range(0, len(currentWord)):
                for c in chars:
                    newWord = currentWord[:i] + c + currentWord[i+1: ]
                    if newWord == endWord:
                        return steps+1
                    if newWord in wordList:
                        wordList.remove(newWord)
                        queue.append([newWord, steps+1])
        return 0

