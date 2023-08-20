# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:

        if not head.next.next:
            return head.val + head.next.val
        if not head:
            return 0


        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        slow_r = self.reverse(slow) 
        curr = head
        currMax = 0

        while slow_r:

            currMax = max(currMax, slow_r.val+curr.val)
            curr = curr.next
            slow_r = slow_r.next

        return currMax

    
            
    def reverse(self, head):
            prev = None
            curr = head
            while curr:
                nextNode = curr.next
                curr.next = prev
                prev = curr
                curr = nextNode
            
            return prev
