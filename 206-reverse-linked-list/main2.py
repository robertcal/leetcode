# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # solved this on my own
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        if not head.next:
            return head

        prev, nxt = head, head.next
        prev.next = None

        while nxt:
            tmp = nxt.next
            nxt.next = prev

            prev = nxt
            nxt = tmp

        return prev