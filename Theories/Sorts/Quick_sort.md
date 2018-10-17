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
        left = 0
        right = end
        while left < right
            while A[left] < pivot and left < right 
                left = left + 1
            end while

            while A[right] > pivot and left < right
                right = right - 1
            end while

            if left < right
                swap(A[left], A[right])
            end if
        end while

        swap(pivot, A[j])
        return i        
    end procedure


    procedure Quick_sort( A : list of sortable items, start, end )
        if start < end
            p = Partition(A, start, end)
            Quick_sort(A, start, p - 1)
            Quick_sort(A, p + 1, end)

    end procedure


### Python enviroment
    - Input type : list
    - Return type : list

