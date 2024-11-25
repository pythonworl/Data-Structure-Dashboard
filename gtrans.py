import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Define a simple graph
def create_graph():
    G = nx.Graph()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'G')]
    G.add_edges_from(edges)
    return G

# BFS algorithm with visualization
def bfs(G, start, plot=False):
    visited = set()
    queue = deque([start])
    order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            order.append(node)
            queue.extend([n for n in G.neighbors(node) if n not in visited])
            if plot:
                plot_graph(G, visited, queue, 'Queue', node)
                st.pyplot(plt)
    return order

# DFS algorithm with detailed visualization
def dfs(G, start, plot=False):
    visited = set()
    stack = [start]
    order = []

    while stack:
        node = stack.pop()  # Remove from stack to process
        if node not in visited:
            visited.add(node)
            order.append(node)
            if plot:
                plot_graph(G, visited, stack, 'Stack', node)
                st.pyplot(plt)
            # Extend stack with unvisited neighbors (reverse order for consistent left-to-right processing)
            for n in reversed(list(G.neighbors(node))):
                if n not in visited:
                    stack.append(n)
    return order

# Updated plotting function to include current node details
def plot_graph(G, visited, frontier, label, current_node=None):
    pos = nx.spring_layout(G)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='white', edge_color='gray')
    nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color='lightblue')
    nx.draw_networkx_nodes(G, pos, nodelist=frontier, node_color='green')
    if current_node:
        plt.title(f"{label} Visualization: {' > '.join(frontier)}\nProcessing node: {current_node}")
    else:
        plt.title(f"{label} Visualization: {' > '.join(frontier)}")

# Streamlit interface
def main():
    st.title("Graph Traversal Demonstration")
    G = create_graph()
    traversal_type = st.selectbox("Choose traversal type", ("BFS", "DFS"))
    start_node = st.selectbox("Choose start node", list(G.nodes()))
    if st.button("Start Traversal"):
        if traversal_type == "BFS":
            st.write("BFS order:", bfs(G, start_node, plot=True))
        else:
            st.write("DFS order:", dfs(G, start_node, plot=True))

if __name__ == "__main__":
    main()
