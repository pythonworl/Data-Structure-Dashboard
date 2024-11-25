import streamlit as st

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, key):
        if key < self.key:
            if self.left is None:
                self.left = TreeNode(key)
            else:
                self.left.insert(key)
        elif key > self.key:
            if self.right is None:
                self.right = TreeNode(key)
            else:
                self.right.insert(key)

    def delete(self, key):
        if key < self.key:
            if self.left:
                self.left = self.left.delete(key)
        elif key > self.key:
            if self.right:
                self.right = self.right.delete(key)
        else:
            if self.left and self.right:
                temp = self.right.find_min()
                self.key = temp.key
                self.right = self.right.delete(temp.key)
            elif self.left:
                return self.left
            else:
                return self.right
        return self

    def find_min(self):
        current = self
        while current.left:
            current = current.left
        return current

    def display_as_html(self):
        node_html = f"<div class='node'>{self.key}</div>"
        if self.left or self.right:
            left_html = self.left.display_as_html() if self.left else "<div class='node empty'></div>"
            right_html = self.right.display_as_html() if self.right else "<div class='node empty'></div>"
            return f"<div class='tree-node'>{node_html}<div class='children'>{left_html}{right_html}</div></div>"
        return f"<div class='tree-node'>{node_html}</div>"

class BinarySearchTree:
    def __init__(self, root=None):
        self.root = TreeNode(root) if root else None

    def insert(self, key):
        if not self.root:
            self.root = TreeNode(key)
        else:
            self.root.insert(key)

    def delete(self, key):
        if self.root:
            self.root = self.root.delete(key)

    def display_tree(self):
        if not self.root:
            return "The tree is empty."
        return self.root.display_as_html()

def load_css():
    css = """
    <style>
        .tree-node, .children {
            display: flex;
            justify-content: center;
            flex-direction: column;
            align-items: center;
        }
        .node {
            width: 60px;
            height: 60px;
            border-radius: 30px;
            background-color: teal;
            color: white;
            display: flex;
            justify-content: center;
            align-items: center;
            margin: 10px 0;
        }
        .children {
            display: flex;
            width: 100%;
            justify-content: space-evenly;
        }
        .empty {
            visibility: hidden;
        }
    </style>
    """
    return css

st.title("Interactive Binary Search Tree Visualization")
st.markdown(load_css(), unsafe_allow_html=True)

if 'bst' not in st.session_state:
    st.session_state.bst = BinarySearchTree()

key = st.number_input("Enter Key", value=0, format="%d")
action = st.selectbox("Choose Action", ["Insert", "Delete"])

if st.button("Execute"):
    if action == "Insert":
        st.session_state.bst.insert(key)
        st.success(f"Inserted {key}")
    elif action == "Delete":
        st.session_state.bst.delete(key)
        st.success(f"Deleted {key}")

tree_html = st.session_state.bst.display_tree()
st.markdown(tree_html, unsafe_allow_html=True)
