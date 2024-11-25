class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def linear_probe_insert(self, key):
        index = self.hash_function(key)
        initial_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == initial_index:
                raise Exception("Hash table is full")
        self.table[index] = key

    def display(self):
        return self.table
import streamlit as st

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash_function(self, key):
        return key % self.size

    def linear_probe_insert(self, key):
        index = self.hash_function(key)
        initial_index = index
        while self.table[index] is not None:
            index = (index + 1) % self.size
            if index == initial_index:
                raise Exception("Hash table is full")
        self.table[index] = key

    def display(self):
        return self.table

st.title('Hash Table with Open Addressing')

# User input for hash table size (M)
mod_value = st.number_input('Enter modulus value (M) for "key mod M":', min_value=1, value=7, step=1)
hash_table = HashTable(mod_value)

# User input for keys
keys_input = st.text_input('Enter keys separated by commas (e.g., 50, 700, 76, 85, 92, 73, 101):')
if st.button('Create Hash Table'):
    try:
        keys = list(map(int, keys_input.split(',')))
        for key in keys:
            hash_table.linear_probe_insert(key)
        st.success("Keys inserted successfully!")
    except Exception as e:
        st.error(str(e))

    # Display the hash table
    st.write("Current Hash Table:")
    st.write(hash_table.display())
