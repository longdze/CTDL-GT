piimport matplotlib.pyplot as plt
import numpy as np


def merge_sort_visualization(arr, left, right, ax):
    if left < right:
        mid = (left + right) // 2

        # Trực quan hóa vùng chia
        ax.plot([left, right], [mid, mid], 'r--', alpha=0.3)
        ax.fill_betweenx([mid, mid + 1], left, right, color='red', alpha=0.1)
        plt.pause(0.5)

        # Đệ quy gọi Merge Sort trên từng nửa danh sách
        merge_sort_visualization(arr, left, mid, ax)
        merge_sort_visualization(arr, mid + 1, right, ax)

        # Trực quan hóa quá trình trộn
        merge_visualization(arr, left, mid, right, ax)
        plt.pause(0.5)


def merge_visualization(arr, left, mid, right, ax):
    i = left
    j = mid + 1
    k = left
    temp = np.copy(arr)

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            temp[k] = arr[i]
            i += 1
        else:
            temp[k] = arr[j]
            j += 1
        k += 1

    while i <= mid:
        temp[k] = arr[i]
        i += 1
        k += 1

    while j <= right:
        temp[k] = arr[j]
        j += 1
        k += 1

    arr[left:right + 1] = temp[left:right + 1]

    # Trực quan hóa quá trình trộn
    ax.cla()
    ax.bar(range(len(arr)), arr, color='blue', alpha=0.5)
    ax.set_title('Merge Sort')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')
    plt.pause(0.1)


# Sử dụng thuật toán Merge Sort để sắp xếp một danh sách
arr = [8, 3, 1, 5, 9, 2, 7, 4, 6]
fig, ax = plt.subplots()
ax.bar(range(len(arr)), arr, color='blue', alpha=0.5)
ax.set_title('Merge Sort')
ax.set_xlabel('Index')
ax.set_ylabel('Value')
plt.pause(1)

merge_sort_visualization(arr, 0, len(arr) - 1, ax)

plt.show()
