# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head
        count = 0
        temp = head
        while temp:
            count += 1
            temp = temp.next
        rotations = k % count
        if rotations == 0:
            return head
        idx = count - rotations
        count = 1
        temp = head
        while count < idx:
            temp = temp.next
            count += 1
        second = temp.next
        temp.next = None
        temp = second
        while temp.next:
            temp = temp.next
        temp.next = head
        return second

        
