# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def find_middle(self, head:Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow
    def mergeTwoSortedLinkedLists(self, left: Optional[ListNode], right: Optional[ListNode]) -> Optional[ListNode]:
        #print(type(left), type(right))
        dummy = ListNode(0)
        temp = dummy
        while left is not None and right is not None:
            if left.val <= right.val:
                temp.next = left
                left = left.next
            else:
                temp.next = right
                right = right.next
            temp = temp.next
        while left:
            temp.next = left
            temp = temp.next
            left = left.next
        while right:
            temp.next = right
            temp = temp.next
            right = right.next
        return dummy.next
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        middle = self.find_middle(head)
        #print(middle.val)
        right = middle.next
        middle.next = None
        left = head
        left = self.sortList(left)
        right = self.sortList(right)
        return self.mergeTwoSortedLinkedLists(left, right)

