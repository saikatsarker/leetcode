from typing import List

class Solution:
    def longestCommonString(self, strs: List[str]) -> str:
        common_string = ''
        substr_in_all_items = False
        str_1 = strs[0]
        for i in range(len(str_1)):
            _char = str_1[i]
            for item in range(1, len(strs)):
                if _char in strs[item] and item >=1 :
                    substr_in_all_items = True
                elif _char not in strs[item] and item >=1 :
                    substr_in_all_items = False
                    break
                else:
                    substr_in_all_items = False
                    break
            if substr_in_all_items:
                common_string += _char
            else:
                i += 1
        
        return common_string
    
    def longestCommonPrefix(self, strs: List[str]) -> str:
        common_string = ''
        for i in range(len(strs[0])):
            common_string += strs[0][i]
            for j in range(1, len(strs)):
                if common_string != strs[j][:i+1] or i+1 >= len(strs[j]):
                    common_string = common_string[:-1]
                    break
        return common_string
            

        
if __name__ == "main":
    # longestCommonString
    Solution().longestCommonString(["flower","flow","flight"])
    Solution().longestCommonString(["flower", "lower", "olo"])
    Solution().longestCommonString(["flower", "lower", "love"])
    Solution().longestCommonString(["flower", "lower", "love", "glow", "olo"])
    Solution().longestCommonString(["lower", "love", "glow", "olo", "flower"])
    Solution().longestCommonString(["flower", "flowerist", "flowless"])
    Solution().longestCommonString(["flower", "flowerist", "lowest"])
    Solution().longestCommonString(["asbjhs", "huhiu", "djh"])
    Solution().longestCommonString(["abc", "def", "ijk"])

    # longestCommonPrefix
    Solution().longestCommonPrefix(['flower', 'flow', 'fly'])
    Solution().longestCommonPrefix(['flower', 'lower', 'fly'])
    Solution().longestCommonPrefix(['asbjhs', 'asbhuhiu', 'asbdjh'])
    Solution().longestCommonPrefix(['abc', 'def', 'ijk'])
    Solution().longestCommonPrefix(['ca', 'a'])