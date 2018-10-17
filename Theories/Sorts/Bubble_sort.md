# Theory of Bubble sort

    - Bubble sort has a worst-case and average complexity of O(n^2) where n is the number of items being sorted.
      When the list is already sorted(best-case), the time complexity of bubble sort is only O(n).
      But still not good algorhitm.
                                            - from Wikipedia


### Pseudocode:
    procedure bubblesort( A : list of sortable items )
        list_length = length(A)
        for i = 0 to list_length - 1
            for j = 1 to list_length
                if A[j - 1] > A[j] then
                    swap(A[j - 1], A[j])
                end if
            end for
        end for
    end procedure


### Python enviroment
    - Input type : list
    - Return type : list


