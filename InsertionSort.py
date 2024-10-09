#Sort the array using insertion sort

class Solution:
    def insert(self, alist, index, n):
        #code here
        pass
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, alist, n):
        #code here
        for i in range(n):
            j = i
            while j > 0 and alist[j] < alist[j - 1]:
                temp = alist[j]
                alist[j] = alist[j - 1]
                alist[j - 1] = temp
                j -= 1
        


#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().split()))

        Solution().insertionSort(arr, n)

        for i in range(n):
            print(arr[i], end=" ")

        print()

# } Driver Code Ends
