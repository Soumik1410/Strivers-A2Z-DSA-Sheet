#User function Template for python3

class Solution:
    def getFloorAndCeil(self, x: int, arr: list) -> list:
        # code here
        ans = []
        arr.sort()
        n = len(arr)
        if arr[0] > x:
            ans.append(-1)
        else:
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] <= x and mid < n - 1 and arr[mid + 1] > x:
                    ans.append(arr[mid])
                    break
                if arr[mid] <= x and mid == n - 1:
                    ans.append(arr[mid])
                    break
                if arr[mid] > x:
                    high = mid - 1
                else:
                    low = mid + 1
            #if high < low and arr[0] <= x:
            #    ans.append(arr[0])
        
        #print(ans)
        
        if arr[n - 1] < x:
            ans.append(-1)
        else:
            low = 0
            high = n - 1
            while low <= high:
                mid = (low + high) // 2
                if arr[mid] >= x and mid > 0 and arr[mid - 1] < x:
                    ans.append(arr[mid])
                    break
                if arr[mid] >= x:
                    high = mid - 1
                else:
                    low = mid + 1
            #if n > 1 and arr[0] < x and arr[1] >= x:
                #ans.append(arr[1])
            if arr[0] >= x:
                ans.append(arr[0])
        
        
        #print(ans)
        return ans

#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():
    t = int(input())
    for _ in range(t):
        x = int(input())
        arr = list(map(int, input().split()))

        ob = Solution()
        ans = ob.getFloorAndCeil(x, arr)
        print(ans[0], ans[1])
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends
