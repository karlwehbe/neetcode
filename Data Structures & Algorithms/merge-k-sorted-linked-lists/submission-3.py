# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        curr = []
        for l in lists:
            curr.append(l)

        nums = [float("inf") for i in range(len(curr))]
        merged_head = ListNode()
        curr_merged = merged_head
        while any(c is not None for c in curr):
            for i in range(len(curr)):
                if curr[i] is not None:
                    nums[i] = curr[i].val
                else:
                    nums[i] = float("inf")

            idx = nums.index(min(nums))
            curr_merged.val = curr[idx].val
            curr[idx] = curr[idx].next

            dummy = ListNode()
            if any(c is not None for c in curr):
                curr_merged.next = dummy
                curr_merged = curr_merged.next

        return merged_head
