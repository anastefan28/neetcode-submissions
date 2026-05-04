
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        node = head
        newHead = None
        prevNode = None
        oldToNew = {}
        while node:
            newNode = Node(node.val)
            oldToNew[node] = newNode
            if not newHead:
                newHead = newNode
            if prevNode:
                prevNode.next = newNode
            prevNode = newNode
            node = node.next
        node = head
        while node:
            newNode = oldToNew[node]
            newNode.random = oldToNew.get(node.random)
            node = node.next
        return newHead
        
        