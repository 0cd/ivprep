#!env python3

'''
Write methods to traverse a binary tree in, pre & post orders.
Also write a method to traverse a tree in level order. Retrieve level along with value.
'''

filterNotNone = lambda iterable: filter(lambda x: x != None, iterable)
def traverse(root, order):
    if root == None: return
    for node in filterNotNone(order(root)):
        if (node is root):
            yield node
        else:
            for descendent in traverse(node, order):
                yield descendent

inOrder   = lambda node: (node.left, node, node.right)
preOrder  = lambda node: (node, node.left, node.right)
postOrder = lambda node: (node.left, node.right, node)

traverseInOrder   = lambda node: traverse(node, inOrder)
traversePreOrder  = lambda node: traverse(node, preOrder)
traversePostOrder = lambda node: traverse(node, postOrder)

def traverseByLevel(root):
    queue = [root]
    levelEdge = root
    level = 0
    while len(queue) > 0:
        node = queue.pop(0)
        yield (level, node)
        queue.extend(node.children)
        if (node is levelEdge and len(node.children)>0):
            level += 1
            levelEdge = node.children[-1]


def main(args):
    from common import sampleBST

    # in order
    print("In Order   :", [node.value for node in traverseInOrder(sampleBST)])

    # pre order
    print("Pre Order  :", [node.value for node in traversePreOrder(sampleBST)])

    # post order
    print("Post Order :", [node.value for node in traversePostOrder(sampleBST)])

    # level
    print("Level      :", ["{0} ({1})".format(node.value, level) for (level, node) in traverseByLevel(sampleBST)])


if __name__ == "__main__":
    import sys
    main(sys.argv)

'''Output
In Order   : [0, 1, 2, 4, 3, 5, 6, 7, 8, 9]
Pre Order  : [5, 4, 1, 0, 2, 3, 7, 6, 9, 8]
Post Order : [0, 2, 1, 3, 4, 6, 8, 9, 7, 5]
Level      : ['5 (0)', '4 (1)', '7 (1)', '1 (2)', '3 (2)', '6 (2)', '9 (2)', '0 (3)', '2 (3)', '8 (3)']
'''