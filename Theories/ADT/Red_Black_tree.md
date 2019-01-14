# Theory of Red Black tree
    Red Black Tree is a kind of Self-balancing binary search tree.
    Each node have color (Red or black). 

    These requirements imposed on a BST the following must be satisfied by a RBT
    1. Each node is either red or black
    2. The root is black. This rule is sometimes omitted. 
       Since the root can always be changed from red to black, 
       but not necessarily vice versa, this rule has little effect on analysis.
    3. All leaves are black.
    4. If a node is red, then both its children are black.
    5. Every path from a given node to any of its descendant leave nodes the same number of black nodes.
        - Frome Wikipedia
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/66/Red-black_tree_example.svg/500px-Red-black_tree_example.svg.png">

    There are 2 special functions on this tree. These are **ReStructuring** and **ReColoring**.
    According to the rule, RBT don't have red node continuously. 
    In other words, red node can't have red node children.
    When this issue happen, one of 2 functions should be operated.
    If uncle node(parent node's sibling node) is black, then **ReStructuring** function operate.
    If uncle node is red, then **ReColoring** function operate.

# ADT of Red-Black Tree
    - Node
        data
        Color
        left_child - Points to left Node
        right_child - Points to right Node
        parent - Points to parent Node

    - Red-Black Tree Functions
        init(self) - Initiate 
        insert(self, data) - insert data in RBT
        delete(self, data) - delete data at RBT
        ReStructuringLeft(self, -) - Restructuring the RBT
        ReStructuringRight(self, -)
        ReColoring(self, -)
        BSTSize(self) - return the size
        is_empty(self) - Check is the RBT empty
        traversal
            - Preorder
            - Postoder
            - Inorder
