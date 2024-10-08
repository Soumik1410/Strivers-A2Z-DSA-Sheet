class Solution:
    def isPalindrome(self, s: str) -> bool:
        final = ""
        for ch in s:
            if ord(ch) >= 65 and ord(ch)<= 90:
                ch = (chr)(32 + ord(ch))
            if ord(ch) >= 97 and ord(ch) <= 122:
                final += str(ch)
            if ord(ch) >= 48 and ord(ch) <= 57:
                final += str(ch)
        
        print(final)
        print(final[::-1])
        if final == final[::-1]:
            return True
        else:
            return False
