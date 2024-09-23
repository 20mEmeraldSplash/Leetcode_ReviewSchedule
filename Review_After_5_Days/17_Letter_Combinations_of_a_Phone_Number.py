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

        def helper(com, current_length):
            if current_length == len(digits):
                result.append(com)
            else:
                for i in phone[digits[current_length]]:
                    helper(com+i, current_length+1)
        helper("", 0)
        return result
            
        return result