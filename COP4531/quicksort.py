"""
Quick and dirty, no edge cases tested
"""


def partitionAroundPivot(A, first, last):
    pivot = A[first]
    lo = first + 1
    hi = last

    while lo < hi:
        # move lo forward until valid swap pos
        while A[lo] <= pivot:
            lo += 1
        # move hi backward until valid swap pos
        while A[hi] > pivot:
            hi -= 1
        if hi <= lo:
            break
        A[lo], A[hi] = A[hi], A[lo]
        lo += 1
        hi -= 1
    # at loop termination, hi will point at last element
    # smaller than pivot, so move pivot to correct place
    A[first], A[hi] = A[hi], A[first]
    return hi

def quickSort(A):
    helper(A, 0, len(A) - 1)
    return A

def helper(A, first, last):
    if first >= last:
        return
    pivotIndex = partitionAroundPivot(A, first, last)
    helper(A, first, pivotIndex - 1)
    helper(A, pivotIndex + 1, last)


if __name__ == "__main__":
    # test parition
    A1 = [4, 1 ,3, 2, 6, 5]
    print(quickSort(A1))
