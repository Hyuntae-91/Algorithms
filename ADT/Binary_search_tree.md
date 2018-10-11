# ADT of Binary Search Tree
    - Node
        data
        left_child - Points to left Node
        right_child - Points to right Node

    - Binary Search Tree Functions
        init(self) - Initiate BST
        insert(self, data) - Insert new node at the BST
        internal_insert(self, root, data) - To set child node as a root node
        delete(self, data) - Delete data at the BST
        search(self, data) - search the data at the tree
        BSTSize(self) - return the size
        is_empty(self) - Check is the BST empty
        traversal
            - Preorder
            - Postoder
            - Inorder
