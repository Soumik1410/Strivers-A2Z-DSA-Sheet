# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverse(self, head, k):
        prev = None
        curr = head
        for i in range(k):
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        #print(prev)
        return prev
    
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy
        curr = head
        while count >= k:
            tail = curr
            for i in range(k):
                curr = curr.next
            new_head = self.reverse(tail, k)
            group_prev.next = new_head
            tail.next = curr
            group_prev = tail
            #print(dummy, new_head)
            count -= k
        return dummy.next

        
