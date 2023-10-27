def merge(B, C):
    output = []
    i, j = 0, 0

    while i < len(B) and j < len(C):
        if B[i] < C[j]:
            output.append(B[i])
            i += 1
        else:
            output.append(C[j])
            j += 1
    
    while i < len(B):
        output.append(B[i])
        i += 1

    while j < len(C):
        output.append(C[j])
        j += 1

    return output

def mergeSort(A):
    
    if len(A) <= 1:
        return A

    median = len(A) // 2
    B = A[:median]
    C = A[median:]

    B = mergeSort(B)
    C = mergeSort(C)

    output = merge(B,C)
    
    return output

# Test
A = [100,99,98,97,90,95,96,91,94,93,92,89,88,87,80,86,85,84,83,82,81]
print(mergeSort(A))