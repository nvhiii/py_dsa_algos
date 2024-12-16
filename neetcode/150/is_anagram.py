class Solution:
    def is_anagram(s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        # counts for each chara
        counts = [0] * 26

        for i in range(len(s)):
            counts[ord(s[i]) - ord("a")] += 1
            counts[ord(t[i]) - ord("a")] -= 1

        for count in counts:
            if count != 0:
                return False
            
        return True
    
    s1, s2 = "racecar", "carrace"
    print(is_anagram(s1, s2))