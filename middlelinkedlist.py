# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # the middle one is most likely to be the length/2
       
        linked_list = [head] #turns head into array so that we can append and get len
        
        while linked_list[-1].next: # while linked list has a next (isnt empty)
            linked_list.append(linked_list[-1].next) # appends vals to list
        return linked_list[len(linked_list) // 2] # middle is len/2, returns middle