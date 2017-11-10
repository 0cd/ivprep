#!env python3

'''
Unival tree - a tree in which all of its nodes have the same value

Examples,

      1
    1   1
    -> is a Unival tree

      1
    2   3
    -> is not a Unival tree

1. Write a function that when given a tree, returns whether it is unival or not

2. Write a function that when given a tree, returns the number of unival subtrees in that tree
      1
    1   2
    -> returns 3

      1
        2
    -> returns 1

--

Solution -
Write a depth-first traversing generator that emits a unival truth value for each node.
Due to the dept-first traversal, the last value emitted is the unival truth value for the root node, that answers (1)
Counting the number of True values answers (2)
'''

def getUnivalTruthValues(node):
    if node.isLeaf:
        yield True
    else:
        univals = ( unival for child in node.children
                               for unival in getUnivalTruthValues(child) )
        for unival in univals:
            yield unival

        yield all(univals) and \
            all(map(lambda child: child.value == node.value, node.children))

def main(args):
    from common import Node
    subTree = \
        Node(1,
            Node(1),
            Node(1)
        )

    tree = \
        Node(1,
            Node(2,
                Node(1),
                Node(1)
            ),
             subTree
        )

    print("is subtree unival?     :", [unival for unival in getUnivalTruthValues(subTree)][-1])
    print("unival sub trees count :", sum((1 for _ in filter(None, getUnivalTruthValues(tree)))))


if __name__=="__main__":
    import sys
    main(sys.argv)

'''Output
is subtree unival?     : True
unival sub trees count : 5
'''