import streamlit as st

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node

    def display(self):
        nodes = []
        current = self.head
        while current:
            address = hex(id(current.next)) if current.next else "None"
            nodes.append(f"Value: {current.data} | Next: {address}")
            current = current.next
        return nodes

    def delete_node(self, key):
        curr_node = self.head
        if curr_node and curr_node.data == key:
            self.head = curr_node.next
            curr_node.next = None  # Ensure node is disconnected
            return True

        prev = None
        while curr_node and curr_node.data != key:
            prev = curr_node
            curr_node = curr_node.next

        if curr_node is None:
            return False

        prev.next = curr_node.next
        curr_node.next = None  # Ensure node is disconnected
        return True

    def search_node(self, key):
        current = self.head
        while current:
            if current.data == key:
                return hex(id(current))  # Return the "address" of the node
            current = current.next
        return None

# Initialize or retrieve the linked list from session state
if 'linked_list' not in st.session_state:
    st.session_state.linked_list = SinglyLinkedList()
    for value in [1, 2, 3]:  # Predefined list with integer values
        st.session_state.linked_list.append(value)

def redraw_linked_list():
    if st.session_state.linked_list.head:
        st.write("Current Linked List:")
        for node_info in st.session_state.linked_list.display():
            st.text(node_info)
    else:
        st.write("The list is currently empty.")

# Streamlit UI setup
st.title("Singly Linked List Operations")
redraw_linked_list()

# Node value input
user_input = st.number_input("Enter an integer value for operations", step=1, format="%d")

# Insertion
if st.button("Insert Node"):
    st.session_state.linked_list.append(user_input)
    st.success(f"Node '{user_input}' inserted!")
    redraw_linked_list()

# Deletion
if st.button("Delete Node"):
    if st.session_state.linked_list.delete_node(user_input):
        st.success(f"Node '{user_input}' deleted!")
        redraw_linked_list()
    else:
        st.error(f"Node '{user_input}' not found!")

# Search
if st.button("Search for Node"):
    address = st.session_state.linked_list.search_node(user_input)
    if address:
        st.success(f"Node '{user_input}' found at address {address}!")
    else:
        st.error(f"Node '{user_input}' not found!")
