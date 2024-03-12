# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        node = head
        sum , res = 0, {}
        while node:
            sum += node.val
            if sum == 0:
                head = node.next
                res = {}
            else:
                if res.get(sum):
                    temp = res[sum].next
                    current_sum = sum
                    while temp != node:
                        current_sum += temp.val
                        del res[current_sum]
                        temp = temp.next
                    res[sum].next = node.next
                else:
                    res[sum] = node
            node = node.next
        return head
