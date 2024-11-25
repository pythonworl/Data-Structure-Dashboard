import tkinter as tk

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, cur_node, key):
        if key < cur_node.val:
            if cur_node.left is None:
                cur_node.left = Node(key)
            else:
                self._insert(cur_node.left, key)
        elif key > cur_node.val:
            if cur_node.right is None:
                cur_node.right = Node(key)
            else:
                self._insert(cur_node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, cur_node, key):
        if cur_node is None:
            return cur_node

        if key < cur_node.val:
            cur_node.left = self._delete(cur_node.left, key)
        elif key > cur_node.val:
            cur_node.right = self._delete(cur_node.right, key)
        else:
            if cur_node.left is None:
                return cur_node.right
            elif cur_node.right is None:
                return cur_node.left

            if cur_node.val < self.root.val:
                temp = self.find_max(cur_node.left)
                cur_node.val = temp.val
                cur_node.left = self._delete(cur_node.left, temp.val)
            else:
                temp = self.find_min(cur_node.right)
                cur_node.val = temp.val
                cur_node.right = self._delete(cur_node.right, temp.val)

        return cur_node

    def find_min(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current

    def inorder_traversal(self, node, result):
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.val)
            self.inorder_traversal(node.right, result)
        return result

    def preorder_traversal(self, node, result):
        if node:
            result.append(node.val)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        return result

    def postorder_traversal(self, node, result):
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.val)
        return result

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()
        self.bst = BinarySearchTree()

    def create_widgets(self):
        self.entry = tk.Entry(self)
        self.entry.pack(side="top", padx=10, pady=10)

        self.insert = tk.Button(self, text="Insert", command=self.insert_node)
        self.insert.pack(side="top", padx=10, pady=5)

        self.delete_btn = tk.Button(self, text="Delete", command=self.delete_node)
        self.delete_btn.pack(side="top", padx=10, pady=5)

        self.inorder_btn = tk.Button(self, text="Show In-order", command=self.show_inorder)
        self.inorder_btn.pack(side="top", padx=10, pady=5)

        self.preorder_btn = tk.Button(self, text="Show Pre-order", command=self.show_preorder)
        self.preorder_btn.pack(side="top", padx=10, pady=5)

        self.postorder_btn = tk.Button(self, text="Show Post-order", command=self.show_postorder)
        self.postorder_btn.pack(side="top", padx=10, pady=5)

        self.result_label = tk.Label(self, text="")
        self.result_label.pack(side="top", padx=10, pady=10)

        self.canvas = tk.Canvas(self, width=800, height=500, bg="white")
        self.canvas.pack(side="bottom", padx=10, pady=10)

    def insert_node(self):
        key = int(self.entry.get())
        self.bst.insert(key)
        self.entry.delete(0, tk.END)
        self.draw_tree()

    def delete_node(self):
        key = int(self.entry.get())
        self.bst.delete(key)
        self.entry.delete(0, tk.END)
        self.draw_tree()

    def show_inorder(self):
        result = []
        self.result_label.config(text="In-order: " + str(self.bst.inorder_traversal(self.bst.root, result)))

    def show_preorder(self):
        result = []
        self.result_label.config(text="Pre-order: " + str(self.bst.preorder_traversal(self.bst.root, result)))

    def show_postorder(self):
        result = []
        self.result_label.config(text="Post-order: " + str(self.bst.postorder_traversal(self.bst.root, result)))

    def draw_tree(self):
        self.canvas.delete("all")
        self.draw_node(self.bst.root, 400, 50, 200)

    def draw_node(self, node, x, y, distance):
        if node:
            self.canvas.create_oval(x-20, y-20, x+20, y+20, fill="skyblue")
            self.canvas.create_text(x, y, text=str(node.val), font=("Helvetica", 15))
            if node.left:
                self.canvas.create_line(x, y, x - distance//2, y + 80)
                self.draw_node(node.left, x - distance//2, y + 80, distance//2)
            if node.right:
                self.canvas.create_line(x, y, x + distance//2, y + 80)
                self.draw_node(node.right, x + distance//2, y + 80, distance//2)

root = tk.Tk()
root.title("Binary Search Tree Visualizer")
app = Application(master=root)
app.mainloop()
