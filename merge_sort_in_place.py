def merge(A, begin, median, end):
    begin2 = median + 1
 
    if (A[median] <= A[begin2]):
        return
 
    while begin <= median and begin2 <= end:
 
        if (A[begin] <= A[begin2]):
            begin += 1
        else:
            value = A[begin2]
            i = begin2
 
            while (i != begin):
                A[i] = A[i - 1]
                i -= 1
 
            A[begin] = value
 
            begin += 1
            median += 1
            begin2 += 1
 
def mergeSort(arr, begin, end):
    if (begin < end):
 
        median = begin + (end - begin) // 2
 
        mergeSort(A, begin, median)
        mergeSort(A, median + 1, end)
 
        merge(A, begin, median, end)

# Test
A = [100,99,98,97,90,95,96,91,94,93,92]
mergeSort(A, 0, len(A) - 1)
print(A)

 
