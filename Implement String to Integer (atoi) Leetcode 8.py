class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if len(s) == 0:
            return 0
        sign = 1
        i = 0
        if s[0] == "-":
            sign = -1
            i = 1
        if s[0] == "+":
            i = 1
        num = 0
        dig = 0
        while i < len(s):
            if ord(s[i]) < 48 or ord(s[i]) > 57:
                break
            dig = ord(s[i]) - 48
            num = num * 10 + dig
            i += 1
        num *= sign
        if num < -1*math.pow(2, 31):
            num = -1*math.pow(2, 31)
        if num > math.pow(2,31) - 1:
            num = math.pow(2,31) - 1
        return int(num)
        
