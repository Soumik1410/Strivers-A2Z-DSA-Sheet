#User function Template for python3


class Solution:
    def sumOfDivisors(self, N):
    	#code here 
    	sum = 0
    	for i in range(N+1):
    	    if i == 0:
    	        continue
            sum = sum + (N // i) * i
        return sum

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        N = int(input())
        ob = Solution()
        ans = ob.sumOfDivisors(N)
        print(ans)
# } Driver Code Ends
