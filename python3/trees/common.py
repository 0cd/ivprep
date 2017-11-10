
class Node:
        def __init__(self, value = None, *children):
            self.value = value
            self.children = children

        @property
        def isLeaf(self):
            return len(self.children) == 0

        @property
        def left(self):
            return self.children[0] if len(self.children)>0 else None

        @property
        def right(self):
            return self.children[1] if len(self.children)>1 else None

sampleBST = \
    Node(5,
         Node(4,
              Node(1,
                   Node(0),
                   Node(2)),
              Node(3)),
         Node(7,
              Node(6),
              Node(9,
                   Node(8))))
