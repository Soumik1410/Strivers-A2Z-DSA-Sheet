#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here 
        pass
    
    def selectionSort(self, arr,n):
        #code here
        for i in range(n):
            min = arr[i]
            pos = i
            for j in range(i+1, n):
                if arr[j] < min:
                    min = arr[j]
                    pos = j
            temp = arr[i]
            arr[i] = min
            arr[pos] = temp

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends
