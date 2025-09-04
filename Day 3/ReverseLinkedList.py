#https://neetcode.io/problems/reverse-a-linked-list?list=neetcode250

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        # original_head = head

        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head
        