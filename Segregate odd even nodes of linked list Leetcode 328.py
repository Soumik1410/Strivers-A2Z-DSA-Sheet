# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None or head.next.next is None:
            return head
        first_odd = head
        first_even = head.next

        ans = ListNode(first_odd.val)
        first_odd = first_odd.next.next
        odd_head = ans
        while first_odd:
            ans.next = ListNode(first_odd.val)
            ans = ans.next
            if first_odd.next:
                first_odd = first_odd.next.next
            else:
                first_odd = first_odd.next
        
        ans = ListNode(first_even.val)
        first_even = first_even.next.next
        even_head = ans
        while first_even:
            ans.next = ListNode(first_even.val)
            ans = ans.next
            if first_even.next:
                first_even = first_even.next.next
            else:
                first_even = first_even.next
        #print(odd_head,even_head)
        curr = odd_head
        while curr.next:
            curr = curr.next
        curr.next = even_head
        return odd_head
            
        
