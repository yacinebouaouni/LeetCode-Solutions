# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        # Empty input lists = []
        if not lists:
            return None

        # Filter out empty lists
        lists = [l for l in lists if l]

        # Remove the case lists = [[]]
        if not lists:
            return None

        # Heap push the values of all the nodes
        heap = []
        for l in lists:
            curr = l
            while curr:
                heapq.heappush(heap, curr.val)
                curr = curr.next

        # Heap pop the min values from the heap and set the next pointer
        head = ListNode(val=heapq.heappop(heap))
        curr = head
        while heap:
            curr.next = ListNode(val=heapq.heappop(heap))
            curr = curr.next
        
        return head
        