class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
    
        # 数字到字母的映射
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl", 
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
    
        # 用来存储结果的列表
        result = []

        def helper(combination, next_digits):
            if len(next_digits) == 0:
                result.append(combination)
            else:
                for letter in phone[next_digits[0]]:
                    helper(combination + letter, next_digits[1:])

        helper("", digits)
        return result