class Solution:
    def myPow(self, x: float, n: int) -> float:
        if x == 0:
            return 0
        sign = 1
        if n < 0:
            sign = -1
            n = -1 * n
        if n == 0:
            return 1
        if n % 2 == 0 and sign == 1:
            return self.myPow(x * x, n // 2)
        if n % 2 == 0 and sign == -1:
            return 1 / self.myPow(x * x, n // 2) 
        if n % 2 == 1 and sign == 1:
            return x * self.myPow(x * x, n // 2)
        if n % 2 == 1 and sign == -1:
            return 1 / (x * self.myPow(x * x, n // 2))
