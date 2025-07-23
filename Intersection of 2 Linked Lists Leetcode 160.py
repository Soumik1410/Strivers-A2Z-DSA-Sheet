# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        count1 = count2 = 0
        curr = headA
        while curr:
            count1 += 1
            curr = curr.next
        curr = headB
        while curr:
            count2 += 1
            curr = curr.next
        slow = fast = None
        if count1 > count2:
            diff = count1 - count2
            slow = headA
            fast = headB
        else:
            diff = count2 - count1
            slow = headB
            fast = headA
        count = 1
        while count <= diff:
            slow = slow.next
            count += 1
        #print(slow, fast)
        while slow and fast:
            if slow == fast:
                return slow            
            slow = slow.next
            fast = fast.next
        return None

        
