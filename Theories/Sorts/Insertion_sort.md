# Theory of Insertion sort

    - Insertion sort has a worst-case complexity of O(n^2) where n is the number of items being sorted.
      But, most case more faster than Bubble sort and Selection sort.
      This sort has O(n) space complexity.
      And In-place sort algorithm.


### Pseudocode:
    procedure Insertion_sort( A : list of sortable items )
        list_length = len(A)
        i = 1
        while i < list_length
            j = i
            while j > 0 and A[j - 1] > A[j]
                swap A[j] and A[j - 1]
                j = j + 1
            end while
            i = i + 1
        end while
    end procedure


### Python enviroment
    - Input type : list
    - Return type : list

