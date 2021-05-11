class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        nums = []
        
        while head:
            nums.append(head.val)
            head = head.next
            
        l, r = 0, len(nums) - 1
        
        while l <= r:
            if nums[l] != nums[r]:
                return False
            l += 1
            r -= 1
        
        return True
