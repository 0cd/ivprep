#!env python3

'''
1. Write a method to find the height of a binary tree
2. Write a method to find if a binary tree is balanced
'''

def height(node):
    if node is None:
        return 0
    else:
        return 1 + max(height(node.left), height(node.right))

def isBalanced(node):
    return (node is None) or (
        isBalanced(node.left) and
        isBalanced(node.right) and
        abs(height(node.left) - height(node.right))<=1
    )

if __name__ == "__main__":
    from common import sampleBST
    print("sampleBST -")
    print("height    :", height(sampleBST))
    print("balanced? :", isBalanced(sampleBST), "\n")

    from common import Node
    unbalancedTree = Node(10, Node(9, sampleBST))
    print("unbalancedTree -")
    print("height    :", height(unbalancedTree))
    print("balanced? :", isBalanced(unbalancedTree), "\n")


'''Output
sampleBST -
height    : 4
balanced? : True 

unbalancedTree -
height    : 6
balanced? : False 
'''
