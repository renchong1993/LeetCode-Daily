class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        d = {char:idx for idx, char in enumerate(S)}
        l, r = 0, 0
        res = []
        
        for idx, char in enumerate(S):
            r = max(r, d[char])
            if r == idx:
                res.append(r - l + 1) 
                l = idx + 1
        return res
