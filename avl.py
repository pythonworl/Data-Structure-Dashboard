import streamlit as st

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key
        self.height = 1

class AVLTree:
    def getHeight(self, node):
        if not node:
            return 0
        return node.height

    def getBalance(self, node):
        if not node:
            return 0
        return self.getHeight(node.left) - self.getHeight(node.right)

    def leftRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def rightRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))
        return y

    def preOrder(self, node):
        res = []
        if node:
            res.append(node.value)
            res = res + self.preOrder(node.left)
            res = res + self.preOrder(node.right)
        return res

def create_left_rotatable_tree():
    root = TreeNode(30)
    root.right = TreeNode(40)
    root.right.right = TreeNode(50)
    return root

def create_right_rotatable_tree():
    root = TreeNode(30)
    root.left = TreeNode(20)
    root.left.left = TreeNode(10)
    return root

def create_left_right_rotatable_tree():
    root = TreeNode(30)
    root.left = TreeNode(20)
    root.left.right = TreeNode(25)
    return root

def create_right_left_rotatable_tree():
    root = TreeNode(30)
    root.right = TreeNode(50)
    root.right.left = TreeNode(40)
    return root


st.title('AVL Tree Rotation Visualizer')

avl = AVLTree()
options = ["Left Rotation", "Right Rotation", "Left-Right Rotation", "Right-Left Rotation"]
choice = st.selectbox("Select rotation type:", options)

if choice == "Left Rotation":
    tree = create_left_rotatable_tree()
    before = avl.preOrder(tree)
    tree = avl.leftRotate(tree)
    after = avl.preOrder(tree)
elif choice == "Right Rotation":
    tree = create_right_rotatable_tree()
    before = avl.preOrder(tree)
    tree = avl.rightRotate(tree)
    after = avl.preOrder(tree)
elif choice == "Left-Right Rotation":
    tree = create_left_right_rotatable_tree()
    before = avl.preOrder(tree)
    tree.left = avl.leftRotate(tree.left)
    tree = avl.rightRotate(tree)
    after = avl.preOrder(tree)
elif choice == "Right-Left Rotation":
    tree = create_right_left_rotatable_tree()
    before = avl.preOrder(tree)
    tree.right = avl.rightRotate(tree.right)
    tree = avl.leftRotate(tree)
    after = avl.preOrder(tree)

st.write(f"Before Rotation: {before}")
st.write(f"After Rotation: {after}")
