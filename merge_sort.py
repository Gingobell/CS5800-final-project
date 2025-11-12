# merge_sort.py
# ---------------------------------------
# Merge Sort implementation (generic)
# ---------------------------------------

def merge_sort(items, key_function):
    """
    Perform merge sort based on the value returned by key_function(item).
    Merge sort is a stable sorting algorithm with O(n log n) complexity.
    """
    if len(items) <= 1:
        return items

    # Split into two halves
    mid = len(items) // 2
    left = merge_sort(items[:mid], key_function)
    right = merge_sort(items[mid:], key_function)

    # Merge two sorted halves
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if key_function(left[i]) <= key_function(right[j]):
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Add remaining items
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged
