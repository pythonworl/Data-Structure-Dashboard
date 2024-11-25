import streamlit as st

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
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
            new_node.prev = last

    def delete_node(self, key):
        curr_node = self.head
        while curr_node:
            if curr_node.data == key:
                if curr_node.prev:
                    curr_node.prev.next = curr_node.next
                if curr_node.next:
                    curr_node.next.prev = curr_node.prev
                if curr_node == self.head:
                    self.head = curr_node.next
                return True
            curr_node = curr_node.next
        return False

    def display(self):
        nodes = []
        current = self.head
        while current:
            prev_addr = hex(id(current.prev)) if current.prev else "None"
            current_addr = hex(id(current))
            next_addr = hex(id(current.next)) if current.next else "None"
            nodes.append(f"Value: {current.data} | Current: {current_addr} | Prev: {prev_addr} | Next: {next_addr}")
            current = current.next
        return nodes

if 'doubly_linked_list' not in st.session_state:
    st.session_state.doubly_linked_list = DoublyLinkedList()
    # Initialize with predefined values
    for value in [1, 2, 3]:
        st.session_state.doubly_linked_list.append(value)

def redraw_linked_list():
    if st.session_state.doubly_linked_list.head:
        st.write("Current Doubly Linked List:")
        for node_info in st.session_state.doubly_linked_list.display():
            st.text(node_info)
    else:
        st.write("The list is currently empty.")

st.title("Doubly Linked List Operations")
redraw_linked_list()
user_input = st.number_input("Enter an integer value for operations", step=1, format="%d")

if st.button("Insert Node"):
    st.session_state.doubly_linked_list.append(user_input)
    st.success(f"Node '{user_input}' inserted!")
    redraw_linked_list()

if st.button("Delete Node"):
    if st.session_state.doubly_linked_list.delete_node(user_input):
        st.success(f"Node '{user_input}' deleted!")
        redraw_linked_list()
    else:
        st.error(f"Node '{user_input}' not found!")
