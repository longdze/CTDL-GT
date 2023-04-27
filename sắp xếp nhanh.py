def sap_xep_nhanh(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        left = []
        right = []
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                left.append(arr[i])
            else:
                right.append(arr[i])
        return sap_xep_nhanh(left) + [pivot] + sap_xep_nhanh(right)
