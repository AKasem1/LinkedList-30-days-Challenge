# https://neetcode.io/problems/palindrome-linked-list?list=neetcode250
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        seen = list()
        count = 0
        if not head:
            return False
        
        while head:
            seen.append(head.val)
            count += 1
            head = head.next
        return seen == seen[::-1]
    

# O(1) space optimal solution
class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = slow = head

        #find middle(slow)
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        #reverse the second half of the list
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp

        #check palindrome
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True