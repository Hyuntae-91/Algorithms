# Theory of Merge sort

    - Merge sort has a worst-case complexity of O(n log n) where n is the number of items being sorted.
      This Algorithm use "Divide and Conquer" strategy.

      This is very efficient, general-purpose, comparison-based sorting algorithm.

      Merge sort works as follows:
      1. Divide the unsorted list into n sublists, each containing 1 element (a list of 1 element is considered sorted)
      2. Repeatedly merge sublists to produce new sorted sublists until there is only 1 sublist remaining. This will be the sorted list
                                                            - Wikipedia


### Pseudocode:
    pseudocode Merge(A, B, C)
        if(A is empty)
            rest of C = rest of B
        else if(B is empty)
            rest of C = rest of A
        else if(first of A <= first of B)
            first of C = first of A
            Merge(rest of A, B, rest of C)
        else
            first of C = first of B
            Merge(A, rest of B, rest of C)
        end if
    end procedure


    procedure Merge_sort( A : list of sortable items, first, last)
        if(first < last)
            mid = (first/last)/2
            Merge_sort(A, first, mid)
            Merge_sort(A, mid+1, last)
            Merge(A, first, mid, last)
        end if
    end procedure


### Python enviroment
    - Input type : list
    - Return type : list

