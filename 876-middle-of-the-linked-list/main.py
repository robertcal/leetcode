# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # solved this on my own
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        middle = head
        move = True
        while head and head.next:
            if move:
                middle = middle.next
                move = False
            else:
                move = True

            head = head.next

        return middle