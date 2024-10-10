def sortedArray(a: [int], b: [int]) -> [int]:
    # Write your code here
    i = 0
    j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] in c:
            i += 1
            continue
        if b[j] in c:
            j += 1
            continue
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
            continue
        if a[i] > b[j]:
            c.append(b[j])
            j += 1
            continue
        if a[i] == b[j]:
            c.append(a[i])
            i += 1
            j += 1
    
    while i < len(a):
        if a[i] in c:
            i += 1
            continue
        else:
            c.append(a[i])
            i += 1
        
    while j < len(b):
        if b[j] in c:
            j += 1
            continue
        else:
            c.append(b[j])
            j += 1
    
    return c
