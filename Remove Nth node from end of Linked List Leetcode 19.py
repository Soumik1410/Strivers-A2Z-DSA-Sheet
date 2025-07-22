# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        total = 1
        curr = head
        while curr.next:
            total += 1
            curr = curr.next
        correct_node = total - n
        if correct_node == 0:
            return head.next
        
        count = 1
        curr = head
        while count < correct_node:
            curr = curr.next
            count += 1
        curr.next = curr.next.next
        return head
