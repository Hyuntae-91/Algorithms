# Theory of Quick sort

    - Quick sort has a worst-case complexity of O(n^2) where n is the number of items being sorted.
      But, Quick sort is really good sorting algorithm. This algorithm occasionally use on Business.
      Worst Case
        1. Array is already sorted in same order
        2. Array is already sortedin reverse order
        3. All elements are same
      
      This Algorithm use "Divide and Conquer" strategy.
      Randomly pick a element as a pivot and divide to "Less than" and "Grater than"

      Also, this algorithm is in-place sort.


### Pseudocode:
    pseudocode Partiton(A : list of sortable items, start, end):
        pivot = A[(start + end) / 2]
        swap(pivot, A[end])
        i = start
        j = end - 1
        while True
            if i > j
                swap(A[i], pivot)
                break
            end if

            if A[i] <= pivot and i <= j
                i = i + 1
            else if A[i] > pivot and i <= j
                j = j - 1

        end while

    end procedure


    procedure Quick_sort( A : list of sortable items )
        list_length = len(A)

    end procedure


### Python enviroment
    - Input type : list
    - Return type : list

