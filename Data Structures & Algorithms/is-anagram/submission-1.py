class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #brute-force solution

        sorted_s = "".join(sorted(s))
        sorted_t = "".join(sorted(t))
    
        if sorted_s == sorted_t:
            return True
        return False


    

