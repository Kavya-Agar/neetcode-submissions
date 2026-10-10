# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        stack2 = []

        curr = l1
        curr2 = l2

        while curr:
            stack.append(curr.val)
            curr = curr.next
            
        while curr2:
            stack2.append(curr2.val)
            curr2 = curr2.next

        num1 = ""
        num2 = ""
        
        while stack:
            num1 += str(stack.pop())
        while stack2:
            num2 += str(stack2.pop())

        total = int(num1) + int(num2)

        if total == 0:
            return ListNode(0)

        head = None
        for char in str(total):
            new_node = ListNode(int(char))
            new_node.next = head
            head = new_node

        return head