class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(i: int, j: int) -> int:
            r = i % j

            if (r == 0):
                return j
            
            return gcd(j, r)

        divisor = gcd(max(len(str1), len(str2)), min(len(str1), len(str2)))
        
        divisorStr = str1[0:divisor]

        if divisorStr * (len(str1) // divisor) == str1 and divisorStr * (len(str2) // divisor) == str2:
            return divisorStr
        else:
            return ""