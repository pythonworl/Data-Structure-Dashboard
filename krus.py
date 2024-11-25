import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush

# Define a simple weighted graph for Kruskal's algorithm
def create_graph_kruskal():
    G = nx.Graph()
    edges = [('A', 'B', 7), ('A', 'D', 5), ('B', 'C', 8),
             ('B', 'D', 9), ('B', 'E', 7), ('C', 'E', 5),
             ('D', 'E', 15), ('D', 'F', 6), ('E', 'F', 8),
             ('E', 'G', 9), ('F', 'G', 11)]
    G.add_weighted_edges_from(edges)
    return G

# Kruskal's algorithm with step-by-step visualization
def kruskal(G, plot=False):
    mst = nx.Graph()
    edges = sorted(G.edges(data=True), key=lambda t: t[2]['weight'])
    sets = {node: node for node in G}
    
    def find(node):
        if sets[node] != node:
            sets[node] = find(sets[node])
        return sets[node]
    
    def union(n1, n2):
        root1 = find(n1)
        root2 = find(n2)
        if root1 != root2:
            sets[root1] = root2

    if plot:
        plot_graph(G, "Initial Graph with Weights", highlight_edges=None)
        st.pyplot(plt)

    for u, v, data in edges:
        if find(u) != find(v):
            mst.add_edge(u, v, weight=data['weight'])
            union(u, v)
            if plot:
                plot_graph(G, "Kruskal's Algorithm Step-by-Step", highlight_edges=mst.edges())
                st.pyplot(plt)
    return mst

# Plotting function with optional edge highlighting
def plot_graph(G, title, highlight_edges):
    pos = nx.spring_layout(G, scale=2)
    plt.figure(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color='green', width=2)
    plt.title(title)

# Streamlit interface
def main():
    st.title("Graph Algorithms Demonstration")
    algorithm = st.selectbox("Choose an algorithm", ("Kruskal's Algorithm", "Prim's Algorithm"))
    G_kruskal = create_graph_kruskal()
    
    if algorithm == "Kruskal's Algorithm":
        if st.button("Compute MST with Kruskal"):
            kruskal(G_kruskal, plot=True)

if __name__ == "__main__":
    main()
