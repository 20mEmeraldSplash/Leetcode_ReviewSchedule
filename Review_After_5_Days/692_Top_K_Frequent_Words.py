import heapq
class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        pq = []
        hashmap = {}

        # 统计每个单词的频率
        for w in words:
            hashmap[w] = hashmap.get(w, 0) + 1

        # 将每个单词及其频率推入堆中，保持堆的大小为 k
        for word, freq in hashmap.items():
            # 使用负频率，使堆按频率降序排列；字母顺序升序
            heapq.heappush(pq, (-freq, word))
        
        # 排序堆中的结果
        pq.sort()  # 按(-freq, word)排序，会先按负频率排，再按字母升序排

        # 结果不需要做任何处理，直接输出前k个
        result = []
        for i in range(k):
            result.append(pq[i][1])

        return result