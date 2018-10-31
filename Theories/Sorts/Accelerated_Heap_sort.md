# Theory of Accelerated Heap sort

Acceleated Heap sort
 - Speed up Heapsort by about a factor of two
   Normal fixHeap costs 2h comparisons in the worst case
   The solution is a surprising application of divide and conquer
    - filter the vacant position halfway down the tree, h/2
    - test whether K is bigger than the parent of vacant
    - Yes : bubble the vacant back up to where K should be
    - No : repeat filter the vacant position another halfway down recursively

 - In theory, the worst case is nlogn + setta(nloglog(n)).
   So, It should be more fast than Heap Sort. Because Heap sort has 2nlog(n) + O(n) worst case.
   But, In real, Acceleated Heap Sort is more slow than Heap sort.
   

### Pseudocode:
    pseudocode bubbleUpHeap(A : list of sortable items, root, key, vacant):
        if vacant is root:
            A[vacant] = key
        else:
            parent = vacant / 2
            if key <= A[parent].key:
                A[vacant] = key
            else
                A[vacant] = A[parent]
                bubbleUpHeap(A, root, key, parent)
            end if
        end if
    end procedure


    pseudocode promote(A : list of sortable items, hStop, vacant, h):
        if h <= hStop:
            vacStop = vacant
        if A[2*vacant].key <= A[2*vacant + 1].key:
            A[vcant] = A[2*vacant + 1]
            vacStop = promote(A, hStop, 2*vacant+1, h-1)
        else:
            A[vcant] = A[2*vcant]
            vacStop = promote(A, hStop, 2*vacant, h-1)
        end if
        return vacStop
    end procedure


    procedure fixHeapFast(A : list of sortable items, key, vacant, h, size)
        if h less than 1:
            process heap of height 0 or 1
        else:
            hStop = h/2
            vacStop = promote(A, hStop, vacant, h) // vacStop is new vacant location, at height hStop
            vacParent = vacStop / 2
            if A[vacParent].key <= key:
                A[vacStop] = A[vacParent]
                bubbleUpHeap(A, vacant, key, vacParent)
            else:
                fixHeapFast(A, key, vacant, h, size)
            end if
        end if
    end procedure


    procedure Accelerated_Heap_sort( A : list of sortable items)
        list_size = (length of A) - 1
        for i = list_size ; i > 0 ; i--:
            curMax = A[1]
            key = A[i]
            fixHeapFast(A, key, 1, --, i -1)
            A[i] = curMax
        end for
    end procedure



### Python enviroment
    - Input type : list
    - Return type : list

