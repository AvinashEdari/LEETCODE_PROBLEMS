class Solution(object):
    def reverseBetween(self, head, left, right):
        if head==None or left==right:
            return head
        prev=None
        temp=head
        for _ in range(left-1):
            prev=temp
            temp=temp.next
        prev1=None
        temp1=temp
        for _ in range(right-left+1):
            next1=temp1.next
            temp1.next=prev1
            prev1=temp1
            temp1=next1
        if prev!=None:
            prev.next=prev1
        else:
            head=prev1
        temp.next=temp1
        return head

         