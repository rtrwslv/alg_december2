class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def __str__(self) -> str:
        return str(str(self.val) + str(self.left) + (str(self.right)))

def trimBST(root: TreeNode, L: int, R: int) -> TreeNode:
    if root==None:
        return root
    if root.val>R:
        return trimBST(root.left,L,R)
    elif root.val<L:
        return trimBST(root.right,L,R)
    root.left=trimBST(root.left,L,R)
    root.right=trimBST(root.right,L,R)
    return root

print(str(trimBST(TreeNode(1, TreeNode(0), TreeNode(2)), 1, 2)))