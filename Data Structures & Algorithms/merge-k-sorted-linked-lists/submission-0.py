# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []
        
        for item in lists:
            while item:
                nodes.append(item.val)
                item = item.next
        
        nodes.sort()
        dummy = ListNode()
        head = dummy
        for i in nodes:
            head.next = ListNode(i)
            head = head.next
        
        return dummy.next