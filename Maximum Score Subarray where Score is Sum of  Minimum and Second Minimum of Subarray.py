#User function Template for python3

class Solution:
    def pairWithMaxSum(self, arr):
        start = 0
        end = 1
        maxi = 0
        while end < len(arr):
            score = arr[start] + arr[end]
            if score > maxi:
                maxi = score
            start += 1
            end += 1
        return maxi
    



#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while (T > 0):
        a = [int(x) for x in input().strip().split()]
        ob = Solution()
        print(ob.pairWithMaxSum(a))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
