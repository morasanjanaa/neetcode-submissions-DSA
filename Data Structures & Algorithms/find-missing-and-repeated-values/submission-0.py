class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = set()
        maxi=grid[0][0]
        a = 0
        b = 0
        for x in grid:
            for i in x:
                if i in ans:
                    a = i
                maxi = max(maxi,i)
                ans.add(i)
        for i in range(1,maxi+1):
            if i not in ans:
                b = i
        if b == 0:
            b = maxi+1
        return [a,b]

        