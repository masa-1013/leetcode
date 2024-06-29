class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        index = 0
        result = ''
        while len(word1) > index or len(word2) > index:
            if (len(word1) > index):
                result += word1[index]
            if (len(word2) > index):
                result += word2[index]
            
            index += 1

        return result
