def areIdentical(head1, head2):
    p1=head1
    p2=head2
    while (p1 is not None  and p2 is not None):
        if p1.data!=p2.data:
            return False
        
        p1=p1.next
        p2=p2.next
    return p1 is None and p2 is None
