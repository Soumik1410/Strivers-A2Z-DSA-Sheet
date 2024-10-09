def removeDuplicates(arr,n):
    # Write your code here.
    count = 1
    for i in range(1, n):
        if arr[i - 1] != arr[i]:
            count += 1
    return count
