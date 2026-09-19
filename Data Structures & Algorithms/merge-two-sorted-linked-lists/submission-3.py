''' The  initial thought is to add all the node values into one list, sort them then sperately  add them into another linked list

Using recursive makes this essenting compares the values of list1 and list2 and sets the next depending on which is smaller but the space complexity is O(n+m)

Using iteration is the better way to go. Iterrate through the linked lists if add the smaller of two in the merged list then move the node pointer in the merge list whilst there are values in both the lists.

'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next

            node = node.next

        node.next = list1 if list2 is None else list2

        return dummy.next

            
        


        