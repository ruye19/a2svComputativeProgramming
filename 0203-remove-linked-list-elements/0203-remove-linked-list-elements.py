# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def removeElements(self, head, val):
        # Step 1: Create a dummy node that points to the head of the list
        dummy = ListNode(-1)
        dummy.next = head
        
        # Step 2: Initialize current and prev pointers
        current = head
        prev = dummy
        
        # Step 3: Traverse the list and remove nodes with the value `val`
        while current:
            if current.val == val:
                # Remove the current node by linking prev to current's next
                prev.next = current.next
            else:
                # Move prev pointer if current node is not removed
                prev = current
            current = current.next
        
        # Step 4: Return the updated list starting from dummy's next (i.e., the new head)
        return dummy.next
