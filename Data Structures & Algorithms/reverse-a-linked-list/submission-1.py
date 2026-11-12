# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ## 0 -> 1 -> 2 -> 3
        ## M    H
        ## 1 -> 0 -> 2 -> 3
        ## 2 -> 1 -> 0 -> 3
        ## 3 -> 2 -> 1 -> 0
        mark = head
        if not mark:
            return head
        while mark.next:
            temp = mark.next
            mark.next = temp.next
            temp.next = head
            head = temp

        
        return head

