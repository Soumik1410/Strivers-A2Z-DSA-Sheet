#User function Template for python3

class Solution:
    def merge(self,arr, l, mid, r):
        # code here
        B = []
        for i in range(l, r+1):
            B.append(0)
        i = l
        j = mid + 1
        k = 0
        while i <= mid and j <= r:
            if arr[i] <= arr[j]:
                B[k] = arr[i]
                k += 1
                i += 1
            else:
                B[k] = arr[j]
                k += 1
                j += 1
        while i <= mid:
            B[k] = arr[i]
            k += 1
            i += 1
        while j <= r:
            B[k] = arr[j]
            k += 1
            j += 1
        
        i = l
        k = 0
        while i <= r:
            arr[i] = B[k]
            i += 1
            k += 1
            
    def mergeSort(self,arr, l, r):
        #code here
        if l < r:
            mid = (l + r) // 2
            self.mergeSort(arr, l, mid)
            self.mergeSort(arr, mid + 1, r)
            self.merge(arr, l, mid, r)



#{ 
 # Driver Code Starts
#Initial Template for Python 3


import sys
input = sys.stdin.readline
if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().mergeSort(arr, 0, n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
