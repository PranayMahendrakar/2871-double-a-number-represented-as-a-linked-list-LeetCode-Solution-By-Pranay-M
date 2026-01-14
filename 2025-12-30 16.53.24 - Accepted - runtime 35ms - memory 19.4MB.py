# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list to process from least significant digit
        def reverse(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        
        # Reverse the list
        head = reverse(head)
        
        # Double each digit and handle carry
        carry = 0
        curr = head
        prev = None
        
        while curr:
            total = curr.val * 2 + carry
            curr.val = total % 10
            carry = total // 10
            prev = curr
            curr = curr.next
        
        # If there's still a carry, add new node
        if carry:
            prev.next = ListNode(carry)
        
        # Reverse back
        return reverse(head)