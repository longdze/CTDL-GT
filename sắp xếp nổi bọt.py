def sap_xep_noi_bot(arr):
    n = len(arr)
    for i in range(n):
        # Duyệt qua từng cặp phần tử liên tiếp và so sánh, hoán đổi nếu cần thiết
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr