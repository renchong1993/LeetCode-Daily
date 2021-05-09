class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1, num2 = 0, 0
       
    
        while l1:
            num1 = num1 * 10 + l1.val
            l1 = l1.next
            
        while l2:
            num2 = num2 * 10 + l2.val
            l2 = l2.next
            
        sums = num1 + num2
        dummy = head = ListNode(0)
        
        if sums == 0:
            return head
        while sums > 0:
            head.next = ListNode(sums % 10)
            head = head.next
            sums //= 10
            
        prev = None
        head = dummy.next
        
        while head:
            nxt = head.next
            head.next = prev
            prev = head
            head = nxt
        
        return prev
