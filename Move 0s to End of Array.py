def moveZeros(n: int,  a: [int]) -> [int]:
    # Write your code here.
    b = []
    count = 0
    for i in range(n):
        if a[i] == 0:
            count += 1
        else:
            b.append(a[i])
    for i in range(count):
        b.append(0)
    return b
