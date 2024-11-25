import streamlit as st

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def breadth_first_traversal(self):
        result = []
        queue = [self]
        while queue:
            current = queue.pop(0)
            result.append(current.value)
            queue.extend(current.children)
        return ' -> '.join(result)

    def depth_first_traversal_pre_order(self):
        result = [self.value]
        for child in self.children:
            result.append(child.depth_first_traversal_pre_order())
        return ' -> '.join(result)

    def depth_first_traversal_post_order(self):
        result = []
        for child in self.children:
            result.append(child.depth_first_traversal_post_order())
        result.append(self.value)
        return ' -> '.join(result)

class Tree:
    def __init__(self, root=None):
        self.root = root

    def display_as_html(self, node):
        if node is None:
            return ""
        if not node.children:
            return f'<li><span class="node">{node.value}</span></li>'
        
        child_str = ''.join([self.display_as_html(child) for child in node.children])
        return f'<li><span class="node">{node.value}</span><ul>{child_str}</ul></li>'

    def render_tree(self):
        if not self.root:
            return "The tree is empty"
        return f'<ul class="tree">{self.display_as_html(self.root)}</ul>'

def create_sample_tree():
    root = TreeNode("Root")
    child1 = TreeNode("Child1")
    child2 = TreeNode("Child2")
    child1.add_child(TreeNode("Grandchild1"))
    child1.add_child(TreeNode("Grandchild2"))
    child2.add_child(TreeNode("Grandchild3"))
    root.add_child(child1)
    root.add_child(child2)
    return Tree(root)

def load_css():
    css = """
    <style>
        body {
            font-family: Arial, sans-serif;
        }
        .tree, .tree ul {
            list-style-type: none;
            position: relative;
            padding: 1em 0;
            white-space: nowrap;
            margin: 0 auto;
            text-align: center;
        }
        .tree li {
            border: 2px solid teal;
            border-radius: 5px;
            padding: 5px 10px;
            display: inline-block;
            color: white;
            background-color: teal;
            position: relative;
            margin: 0 5px;
            line-height: 1.5em;
        }
        .tree ul ul::before {
            content: '';
            position: absolute;
            top: 0;
            width: 0px;
            height: 100%;
            border-left: 2px solid black;
        }
    </style>
    """
    return css

st.title("Interactive Tree Visualization and Traversal")
st.markdown(load_css(), unsafe_allow_html=True)

tree = create_sample_tree()
tree_html = tree.render_tree()
st.markdown(tree_html, unsafe_allow_html=True)

traversal_type = st.selectbox("Choose traversal type:", ["Breadth-First", "Depth-First Pre-Order", "Depth-First Post-Order"])
if st.button("Perform Traversal"):
    if traversal_type == "Breadth-First":
        result = tree.root.breadth_first_traversal()
    elif traversal_type == "Depth-First Pre-Order":
        result = tree.root.depth_first_traversal_pre_order()
    else:
        result = tree.root.depth_first_traversal_post_order()
    st.write(f"Traversal result: {result}")
