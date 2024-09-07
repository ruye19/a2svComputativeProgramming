# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head or not head.next:
            return True
        
        stack = []
        slow, fast = head, head
        
        # Push the first half of the elements onto the stack
        while fast and fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        # If the list has an odd number of elements, skip the middle element
        if fast:
            slow = slow.next
        
        # Compare the second half with the elements in the stack
        while slow:
            if stack.pop() != slow.val:  # Fix: `stack.pop()` as a function call
                return False
            slow = slow.next
        
        return True
