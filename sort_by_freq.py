def custom_sort_by_frequency(arr):
    frequency_dict = {}
    for num in arr:
        if num in frequency_dict:
            frequency_dict[num] += 1
        else:
            frequency_dict[num] = 1

    sorted_arr = sorted(arr, key=lambda x: (frequency_dict[x], arr.index(x)))

    return sorted_arr

# Example usage
arr = [4, 5, 6, 4, 4, 5, 7, 8, 6, 4, 5]
sorted_arr = custom_sort_by_frequency(arr)
print(sorted_arr)
