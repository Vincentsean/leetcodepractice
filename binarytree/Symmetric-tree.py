# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def go(self, root, layer, stack):
        if root:
            try:
                stack[layer].append(root.val)
            except:
                stack.append([])
                stack[layer].append(root.val)
            layer += 1
            stack = self.go(root.left, layer, stack)
            stack = self.go(root.right, layer, stack)
        else:
            try:
                stack[layer].append('e')
            except:
                stack.append([])
                stack[layer].append('e')
        return stack  
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        stack, layer = [], 0
        stack = self.go(root, layer, stack)
        print (stack)
        for i in stack:
            t = i.copy()
            t.reverse()
            if i == t:
                pass
            else:
                return False
        return True
    
    
    
class Solution2:
    def go(self, right, left):
        if (right==None) and (left!=None):
            return False
        elif (right!=None) and (left==None):
            return False
        elif (right==None) and (left==None):
            return True
        elif right.val != left.val:
            return False
        else:
            return (self.go(right.right, left.left))and (self.go(right.left, left.right))
            
        
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        else:
            return self.go(root.right, root.left)
