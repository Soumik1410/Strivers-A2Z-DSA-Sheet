#User function Template for python3

class Solution:
    def lenOfLongSubarr (self, arr, n, k) :
        mydict = {}
        mydict[0] = -1
        sum = 0
        result = 0
        for i in range(n):
            sum += arr[i]
            diff = sum - k
            if diff in mydict:
                idx = mydict[diff]
                result = max(result, i - idx)
            if sum not in mydict:
                mydict[sum] = i
        #print(mydict)
        return result


#{ 
 # Driver Code Starts
#Initial Template for Python 3


for _ in range(0,int(input())):
    
    n, k = map(int , input().split())
    arr = list(map(int,input().strip().split()))
    ob = Solution()
    print(ob.lenOfLongSubarr(arr, n, k))




# } Driver Code Ends
