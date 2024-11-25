import streamlit as st
import time

# Function for linear search
def linear_search(arr, x):
    for i in range(len(arr)):
        # Highlight current element being checked
        st.write(f"Checking element at index {i}: {arr[i]}")
        time.sleep(1)
        if arr[i] == x:
            return i
    return -1

# Function for binary search (assuming array is sorted)
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2
        # Highlight current mid and range being checked
        st.write(f"Checking element at index {mid}: {arr[mid]}")
        time.sleep(1)
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Streamlit UI
def main():
    st.title("Search Algorithms")

    search_algorithm = st.selectbox("Select search algorithm", ["Linear Search", "Binary Search"])

    if search_algorithm == "Linear Search":
        st.write("You selected Linear Search")
        arr = st.text_input("Enter space-separated array elements")
        x = st.text_input("Enter element to search")
        if st.button("Search"):
            arr = list(map(int, arr.split()))
            x = int(x)
            result = linear_search(arr, x)
            if result != -1:
                st.write(f"Element {x} found at index {result}")
            else:
                st.write(f"Element {x} not found in the array")

    elif search_algorithm == "Binary Search":
        st.write("You selected Binary Search")
        arr = st.text_input("Enter space-separated sorted array elements")
        x = st.text_input("Enter element to search")
        if st.button("Search"):
            arr = list(map(int, arr.split()))
            x = int(x)
            result = binary_search(arr, x)
            if result != -1:
                st.write(f"Element {x} found at index {result}")
            else:
                st.write(f"Element {x} not found in the array")

if __name__ == "__main__":
    main()