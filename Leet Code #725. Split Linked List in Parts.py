class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        res = []
        leng = 0
        main_curr = root
        
        while main_curr:
            leng += 1
            main_curr = main_curr.next
        
        main_curr = root
         
        q = leng // k 
        r = leng % k 
        prev = None 
        
        for _ in range(k):
            if main_curr: 
                res.append(main_curr)
                if r > 0: 
                    parts = q + 1
                    r -= 1
                else:
                    parts = q
                for _ in range(parts):
                    prev = main_curr
                    main_curr = main_curr.next 
                prev.next = None 
            else:
                res.append(None)

        return res
