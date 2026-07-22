# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1, head2 = list1, list2
        curr1, curr2 = head1, head2

        head_of_list = 0
        if head1 is None:
            return head2
        elif head2 is None:
            return head1
        
        if head1.val <= head2.val:
            dummy = curr1
            curr1 = curr1.next
            head_of_list = 1
        else:
            dummy = curr2
            curr2 = curr2.next
            head_of_list = 2
        
        
        while curr1 is not None or curr2 is not None:
            if curr1 is None:
               dummy.next = curr2
               dummy = dummy.next
               curr2 = curr2.next
            elif curr2 is None:
                dummy.next = curr1
                dummy = dummy.next
                curr1 = curr1.next
            elif curr1.val <= curr2.val:
                print("dummy will point to", curr1.val)
                dummy.next = curr1
                dummy = dummy.next
                curr1 = curr1.next
            else:
               print("dummy will point to", curr2.val)
               dummy.next = curr2
               dummy = dummy.next
               curr2 = curr2.next

            print("$$$$$$$")
        
        if head_of_list == 1:
            return head1
     
        return head2

            
                
            