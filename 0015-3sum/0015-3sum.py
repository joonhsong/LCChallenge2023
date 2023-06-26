class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n, z, p = [], [], []
        ret = set()
        
        for i in nums:
            if i < 0:
                n.append(i)
            elif i == 0:
                z.append(i)
            elif i > 0:
                p.append(i)
        
        neg, pos = set(n), set(p)
        
        if len(z) >= 3:
            ret.add((0,0,0))
        
        if z:
            for i in pos:
                if -i in neg:
                    ret.add((-i, 0, i))
        
        for i in range(len(n)):
            for j in range(i+1,len(n)):
                target = -1*(n[i]+n[j])
                if target in pos:
                    ret.add(tuple(sorted([n[i],n[j],target])))

        for i in range(len(p)):
            for j in range(i+1,len(p)):
                target = -1*(p[i]+p[j])
                if target in neg:
                    ret.add(tuple(sorted([p[i],p[j],target])))
        return ret
                
         