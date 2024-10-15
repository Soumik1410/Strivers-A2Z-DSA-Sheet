class Solution:
    #Back-end complete function Template for Python 3
    
    #Function to find the leaders in the array.
    def leaders(self,n, a):
        #Code here
        n = len(a)
        leaders = []
        leaders.append(a[n - 1])
        max = a[n - 1]
        for i in range(n - 2, -1, -1):
            if a[i] >= max:
                leaders.append(a[i])
                max = a[i]
            i -= 1
        leaders.reverse()
        return leaders


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():

    T = int(input())

    while (T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        obj = Solution()

        A = obj.leaders(N, A)

        for i in A:
            print(i, end=" ")
        print()

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends
