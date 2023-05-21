def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Chia danh sách thành hai nửa
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Đệ quy gọi Merge Sort trên từng nửa danh sách
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Trộn hai nửa danh sách đã được sắp xếp lại với nhau
    return merge(left_half, right_half)


def merge(left, right):
    result = []
    i = j = 0

    # So sánh từng phần tử của hai nửa danh sách và chèn vào danh sách kết quả
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    # Chèn các phần tử còn lại từ nửa danh sách chưa trống vào danh sách kết quả
    result.extend(left[i:])
    result.extend(right[j:])

    return result


# Sử dụng thuật toán Merge Sort để sắp xếp một danh sách
arr = [8, 3, 1, 5, 9, 2, 7, 4, 6]
sorted_arr = merge_sort(arr)
print(sorted_arr)
