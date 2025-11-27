class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        prefix = ""
        if not strs:
            return prefix

        #starting with the first lettter, check that all strings have the same letter
        for i in range(len(strs[0])):


            char = strs[0][i]
            for string in strs:
                if i >= len(string) or string[i] != char:
                    return prefix
            prefix += char

        return prefix