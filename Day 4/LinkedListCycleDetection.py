# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return False
        slow_pointer = head
        fast_pointer = head.next.next

        if not fast_pointer:
            return False
        else:
            while fast_pointer:
                if slow_pointer == fast_pointer:
                    return True
                if fast_pointer.next and fast_pointer.next.next:
                    fast_pointer = fast_pointer.next.next
                    slow_pointer = slow_pointer.next
                else:
                    return False
            return False