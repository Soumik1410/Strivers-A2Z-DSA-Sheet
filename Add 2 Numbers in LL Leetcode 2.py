# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        temp1 = l1
        temp2 = l2
        ans = ListNode(0)
        temp = ans
        carry = sum = 0
        while temp1 and temp2:
            sum = temp1.val + temp2.val + carry
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(sum)
            temp = temp.next
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1:
            sum = temp1.val + carry
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(sum)
            temp = temp.next
            temp1 = temp1.next
        while temp2:
            sum = temp2.val + carry
            if sum >= 10:
                sum = sum % 10
                carry = 1
            else:
                carry = 0
            temp.next = ListNode(sum)
            temp = temp.next
            temp2 = temp2.next
        if carry == 1:
            temp.next = ListNode(1)
        return ans.next
            
        
