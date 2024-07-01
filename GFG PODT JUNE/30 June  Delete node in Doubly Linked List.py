class Solution:
    def delete_node(self, head, x):
        if not head or x <= 0:
            return head
        
        if x == 1:
            new_head = head.next
            if new_head:
                new_head.prev = None
            return new_head
        
        pre = None
        curr = head
        for i in range(1, x):
            pre = curr
            curr = curr.next
            if curr is None:
                return head
        
        if pre:
            pre.next = curr.next
        if curr.next:
            curr.next.prev = pre
        
        return head
        #code here
