import streamlit as st
import time

def bubble_sort(arr):
    n = len(arr)
    steps = []
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the array from 0 to n-i-1
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # Append current state of the array to the steps list
                steps.append(list(arr))
    return steps

def insertion_sort(arr):
    steps = []
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        steps.append(list(arr))
    return steps

def selection_sort(arr):
    steps = []
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        steps.append(list(arr))
    return steps

def radix_sort(arr):
    steps = []
    max_value = max(arr)
    exp = 1
    while max_value // exp > 0:
        counting_sort(arr, exp, steps)
        exp *= 10
    return steps

def counting_sort(arr, exp, steps):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
    steps.append(list(arr))

def merge_sort(arr):
    steps = []
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1
        steps.append(list(arr))
    return steps

def quick_sort(arr):
    steps = []
    quick_sort_helper(arr, 0, len(arr) - 1, steps)
    return steps

def quick_sort_helper(arr, low, high, steps):
    if low < high:
        pi = partition(arr, low, high, steps)
        quick_sort_helper(arr, low, pi - 1, steps)
        quick_sort_helper(arr, pi + 1, high, steps)

def partition(arr, low, high, steps):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    steps.append(list(arr))
    return i + 1

def counting_sort_wrapper(arr):
    steps = []
    max_value = max(arr)
    counts = [0] * (max_value + 1)
    for num in arr:
        counts[num] += 1
    sorted_arr = []
    for i in range(len(counts)):
        sorted_arr.extend([i] * counts[i])
        steps.append(list(sorted_arr))
    return steps

def main():
    st.title("Sorting Algorithm Live Visualization")

    algorithm = st.selectbox("Select Sorting Algorithm", ("Bubble Sort", "Insertion Sort", "Selection Sort",
                                                          "Radix Sort", "Merge Sort", "Quick Sort", "Counting Sort"))

    # User input for array
    arr = st.text_input("Enter array of numbers separated by spaces:")

    if st.button("Sort"):
        # Convert input string to list of integers
        arr = [int(x) for x in arr.split()]

        # Perform sorting and get steps
        if algorithm == "Bubble Sort":
            steps = bubble_sort(arr)
        elif algorithm == "Insertion Sort":
            steps = insertion_sort(arr)
        elif algorithm == "Selection Sort":
            steps = selection_sort(arr)
        elif algorithm == "Radix Sort":
            steps = radix_sort(arr)
        elif algorithm == "Merge Sort":
            steps = merge_sort(arr)
        elif algorithm == "Quick Sort":
            steps = quick_sort(arr)
        else:
            steps = counting_sort_wrapper(arr)

        # Display sorting process step by step
        for i, step in enumerate(steps):
            st.write(f"Step {i+1}: {step}")
            time.sleep(1)  # Delay for visualization

if __name__ == "__main__":
    main()

