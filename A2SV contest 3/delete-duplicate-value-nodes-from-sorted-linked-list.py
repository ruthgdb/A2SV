#
# Complete the 'removeDuplicates' function below.
#
# The function is expected to return an INTEGER_SINGLY_LINKED_LIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST llist as parameter.
#

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def removeDuplicates(llist):
    # Write your code here
    if not llist:
            return llist
        
    temp = llist
        
    while llist.next:
        if llist.data == llist.next.data:
            llist.next = llist.next.next
        else:
            llist = llist.next
        
    return temp