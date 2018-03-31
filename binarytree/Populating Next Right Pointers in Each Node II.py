# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            p, q, nextN = root, None, None
            while p:
                if p.left:
                    if q: q.next = p.left
                    q = p.left
                    if nextN == None:
                        nextN = p.left
                if p.right:
                    if q: q.next = p.right
                    q = p.right
                    if nextN == None:
                        nextN = p.right
                    
                p = p.next
                
            self.connect(nextN)
                
