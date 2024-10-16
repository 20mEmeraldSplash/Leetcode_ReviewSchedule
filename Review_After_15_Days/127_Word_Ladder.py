import collections
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
        q = collections.deque()
        q.append([beginWord, 1])
        chars = 'abcdefghijklmnopqrstuvwxyz'

        while q:
            currW, currS = q.popleft()
            for i in range(0, len(currW)):
                for c in chars:
                    newW = currW[:i] + c + currW[i+1:]
                    if newW == endWord:
                        return currS + 1
                    if newW in wordList:
                        wordList.remove(newW)
                        q.append([newW, currS + 1])
        return 0


        