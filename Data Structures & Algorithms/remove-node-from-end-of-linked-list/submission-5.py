# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        count = 1

        while curr.next:
            curr = curr.next
            count+=1

        toGo = count - n

        if toGo == 0:
            if head.next is None:
                head = None
                return head
            head = head.next
            return head

        i = 0
        curr = head
        while i < toGo - 1:
            curr = curr.next
            i+=1
        

        nodeGone = curr.next
        newLast = nodeGone.next
        curr.next = newLast
        nodeGone.next = None
        return head