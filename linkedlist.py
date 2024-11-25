import streamlit as st

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insert_at_position(self, data, position):
        if position == 0:
            self.insert_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return
            current = current.next
        if current is None:
            return
        new_node.next = current.next
        current.next = new_node

    def delete(self, data):
        temp = self.head
        if temp is not None:
            if temp.data == data:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        while current:
            st.write(current.data, end=" -> ")
            current = current.next
        st.write("None")

def main():
    st.title("Linked List Implementation using Streamlit")

    # Initialize a predefined linked list
    predefined_linked_list = LinkedList()
    predefined_linked_list.insert_end("Apple")
    predefined_linked_list.insert_end("Banana")
    predefined_linked_list.insert_end("Cherry")

    st.sidebar.subheader("Predefined Linked List")
    predefined_linked_list.display()

    linked_list = LinkedList()

    st.sidebar.subheader("Operations")
    option = st.sidebar.selectbox("Select Operation", ("Insert Beginning", "Insert End", "Insert at Position", "Delete", "Search", "Display"))

    if option == "Insert Beginning":
        data = st.text_input("Enter data to insert at the beginning:")
        if st.button("Insert Beginning"):
            predefined_linked_list.insert_beginning(data)
            st.success(f"Inserted {data} at the beginning.")

    elif option == "Insert End":
        data = st.text_input("Enter data to insert at the end:")
        if st.button("Insert End"):
            predefined_linked_list.insert_end(data)
            st.success(f"Inserted {data} at the end.")

    elif option == "Insert at Position":
        data = st.text_input("Enter data to insert:")
        position = st.number_input("Enter position to insert:", min_value=0, step=1)
        if st.button("Insert at Position"):
            predefined_linked_list.insert_at_position(data, position)
            st.success(f"Inserted {data} at position {position}.")

    elif option == "Delete":
        data = st.text_input("Enter data to delete:")
        if st.button("Delete"):
            predefined_linked_list.delete(data)
            st.success(f"Deleted {data} from the linked list.")

    elif option == "Search":
        data = st.text_input("Enter data to search:")
        if st.button("Search"):
            if predefined_linked_list.search(data):
                st.success(f"Found {data} in the linked list.")
            else:
                st.warning(f"{data} not found in the linked list.")

    elif option == "Display":
        st.write("Linked List:")
        predefined_linked_list.display()

    # Display the current state of the predefined linked list
    st.sidebar.subheader("Current Linked List")
    current = predefined_linked_list.head
    while current:
        st.sidebar.write(current.data)
        current = current.next

if __name__ == "__main__":
    main()