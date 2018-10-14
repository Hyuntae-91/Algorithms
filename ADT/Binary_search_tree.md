# ADT of Binary Search Tree
    - Node
        data
        left_child - Points to left Node
        right_child - Points to right Node

    - Binary Search Tree Functions
        init(self) - Initiate BST
        insert(self, data) - Wrapper function
        delete(self, data) - Wrapper function
        LeftMostNode(self, root) - Search Min Node at the Tree to delete data
        replace_Node(self, replace, new)
        BSTSize(self) - return the size
        is_empty(self) - Check is the BST empty
        traversal
            - Preorder
            - Postoder
            - Inorder
