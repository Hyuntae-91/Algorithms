# ADT of Binary Search Tree
    - Node
        data
        left_child - Points to left Node
        right_child - Points to right Node

    - Binary Search Tree Functions
        init(self) - Initiate BST
        insert(self, data) - Wrapper function
        internal_insert(self, root, data) - insert Node at the BST
        delete(self, data) - Wrapper function
        internal_delete(self, root, data) - Delete data at the BST
        FindMinNode(self, root) - Search Min Node at the Tree to delete data
        BSTSize(self) - return the size
        is_empty(self) - Check is the BST empty
        traversal
            - Preorder
            - Postoder
            - Inorder
