#User function Template for python3


class Solution:
    def evenlyDivides (self, N):
        # code here
        count = 0
        num = N
        while num!=0:
            dig = num % 10
            if dig != 0 and N % dig == 0:
                count = count + 1
            num = num // 10
        
        return count

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends
