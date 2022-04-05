class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output=[]
        stack=[]
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                holder=stack.pop()
                output.append(holder.val)
                root=holder.right
        return output

                
        
