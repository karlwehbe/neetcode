class Node:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def print_list(head):
    node = head
    while node:
        print("list:", node.val, end=" -> " if node.next else "\n")
        node = node.next


class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next

        groups = length // k

        new_head = None
        prev_group_tail = None
        curr = head

        for g in range(groups):
            group_tail = curr
            prev = None
            for _ in range(k):
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            if g == 0:
                new_head = prev
            else:
                prev_group_tail.next = prev

            prev_group_tail = group_tail

        prev_group_tail.next = curr

        return new_head if groups > 0 else head