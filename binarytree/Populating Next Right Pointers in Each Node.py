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
        if root and root.left:
            root.left.next = root.right
            if root.next:
                root.right.next = root.next.left
            
            self.connect(root.left)
            self.connect(root.right)
            
        
        
class Solution2:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root or not root.left:
            return
        
        
        
        L = root.left
        R = root.right
        while L :
            L.next = R
            L = L.right
            R = R.left
        self.connect(root.right)
        self.connect(root.left)
        
