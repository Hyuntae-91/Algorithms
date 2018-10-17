# Theory of Selection sort

    - Selection sort has a worst-case complexity of O(n^2) where n is the number of items being sorted.
                                            - from Wikipedia


### Pseudocode:
    procedure Selectionsort( A : list of sortable items )
        list_length = length(A)
        for i = 0 to list_length - 1
            min = unsorted_list[i]
            for j = 1 to list_length
                if min > unsorted_list[j]
                    min = unsorted_list[j]
                end if
            end for
            unsorted_list[i], min = min, unsorted_list[i]
        end for
    end procedure


### Python enviroment
    - Input type : list
    - Return type : list


