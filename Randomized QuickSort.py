#User function Template for python3
import random
class Solution:
    #Function to sort a list using quick sort algorithm.
    def quickSort(self,arr,low,high):
        if low < high:
            k = random.randint(low, high)
            temp = arr[k]
            arr[k] = arr[low]
            arr[low] = temp
            p = self.partition(arr, low, high)
            self.quickSort(arr, low, p - 1)
            self.quickSort(arr, p + 1, high)
    
    def partition(self,arr,low,high):
        pivot = arr[low]
        i = low + 1
        j = high
        while i <= j:
            while i <=j and arr[i] <= pivot:
                i += 1
            while i <= j and arr[j] > pivot:
                j-=1
            if i < j:
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
                i += 1
                j -= 1
        i -= 1
        arr[low] = arr[i]
        arr[i] = pivot
        return i


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
        Solution().quickSort(arr,0,n-1)
        for i in range(n):
            print(arr[i],end=" ")
        print()

# } Driver Code Ends
