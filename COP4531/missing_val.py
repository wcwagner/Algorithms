import math
def find_missing_val(A):

    # case that n+1 is missing
    if A[len(A) - 1] == len(A) - 1:
        return len(A)
    hi = len(A) - 1
    lo = 0
    mid = 0
    while mid < hi:

        mid = int(math.ceil((float(hi) + float(lo)) / 2))
        print(lo, mid, hi)
        if A[hi] - A[mid] > hi - mid:
            lo = mid
        elif A[mid] - A[lo] > mid - lo:
            hi = mid

    return hi + 1



if __name__ == "__main__":

    # 7
    print(find_missing_val([0, 1, 2, 3, 4, 5, 6]))

    # 2
    print(find_missing_val([0, 1, 3, 4, 5, 6, 7]))

    # 5
    print(find_missing_val([0, 1, 2, 3, 4, 6, 7]))

    print(find_missing_val([0]))


