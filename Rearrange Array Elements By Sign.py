class Solution:
    def rearrangeArray(self, a: List[int]) -> List[int]:
        b = []
        c = []
        d = []
        for x in a:
            if x < 0:
                b.append(x)
            else:
                c.append(x)
        
        i = 0
        j = 0
        k = 0
        #print(b)
        #print(c)
        while i < 2*len(b):
            if i % 2 == 0:
                d.append(c[j])
                j += 1
            else:
                d.append(b[k])
                k += 1
            i += 1
        return d
