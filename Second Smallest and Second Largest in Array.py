def getSecondOrderElements(n: int,  a: [int]) -> [int]:
    # Write your code here.
    result = []
    b = []
    b.extend(a)
    l = 0
    for i in range(n):
        if b[i] > b[l]:
            l = i
    b[l] = -1
    sl = b[0]
    for i in range(n):
        if b[i] > sl:
            sl = b[i]
    result.append(sl)

    c = []
    c.extend(a)
    s = 0
    for i in range(n):
        if c[i] < c[s]:
            s = i
    c[s] = 10**9 + 1
    ss = c[0]
    for i in range(n):
        if c[i] < ss:
            ss = c[i]
    result.append(ss)

    return result



