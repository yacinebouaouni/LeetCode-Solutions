# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        length = 1
        tail = head
        while tail.next:
            length += 1
            tail = tail.next
        
        k = k % length 
        if k == 0:
            return head
            

        tail.next = head
        for _ in range(length-k-1):
            head = head.next

        new_head = head.next
        head.next = None
        return new_head