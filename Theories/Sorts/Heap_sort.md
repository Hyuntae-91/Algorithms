# Theory of Heap sort

Heap
 - Heap data structure is a binary tree with special properties.
   When the following conditions are satisfied, we can call a binary tree(T) as a Heap structure
        - T is complete at least through depth h - 1
        - All leaves are at depth h or h - 1
        - All path to a leaf of depth h are to the left of all paths to a leaf of depth h - 1

Heap sort
 - This sort algorithm has nlogn worst case runtime.
   If the elements to be sorted are arranged in a heap(Min or Max)
    - We can build a sorted sequence in reverse order by repeatedly removing the element from the root
    - Rearranging the remaining elements to reestablish the partial order tree property, and so on.
   

### Pseudocode:
    pseudocode Construct_heap(A : list of sortable items, root, size):
        if root node is leaf node:
            Construct_heap(A, Left sub tree, size)
            Construct_heap(A, Right sub tree, size)
            key = A[root]
            fixHeap(A, root, key, size)
        end if
    end procedure


    pseudocode fixHeap(A : list of sortable items, root, key, size):
        if root node is leaf node:
            A[root] = key
        else:
            LargerSubHeap = Left Subtree
            if Right subtree is exist and larger than left subtree:
                LargerSubHeap = Right Subtree
            end if

            if key is larger than Right Subtree's data:
                A[root] = key
            else:
                A[root] = A[LargerSubHeap]
                fixHeap(A, root, key, size)
            end if
        end if
    end procedure


    procedure Heap_sort(A : list of sortable items)
        list_size = (length of A) - 1
        Construct_heap(A, 0, list_size)

        for i = list_size ; i > 0 ; i--:
            curMax = A[0]
            key = A[i]
            fixHeap(A, 0, key, i)
            A[i] = curMax
        end for

        return A
    end procedure


### Python enviroment
    - Input type : list
    - Return type : list

