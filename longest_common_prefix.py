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
        substr_in_all_items = False
        for i in range(len(strs[0])):
            for j in range(1, len(strs)):
                print(strs[j])
                if strs[0][:i] in strs[j][:i]:
                    substr_in_all_items = True
                else:
                    substr_in_all_items = False
                    break
                
            if substr_in_all_items:
                common_string += strs[0][:i]
                print("--->"+common_string)
            

        
if __name__ == "main":

    Solution().longestCommonPrefix(['flower', 'lower', 'lowest'])
    Solution().longestCommonPrefix(['flower', 'lower', 'olo'])
    Solution().longestCommonPrefix(['flower', 'lower', 'love'])
    Solution().longestCommonPrefix(['flower', 'lower', 'love', 'glow', 'olo'])
    Solution().longestCommonPrefix(['lower', 'love', 'glow', 'olo', 'flower'])
    Solution().longestCommonPrefix(['flower', 'flowerist', 'flowless'])
    Solution().longestCommonPrefix(['flower', 'flowerist', 'lowest'])
    Solution().longestCommonPrefix(['asbjhs', 'huhiu', 'djh'])
    Solution().longestCommonPrefix(['abc', 'def', 'ijk'])