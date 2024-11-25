import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from heapq import heappop, heappush, heapify 

 # This line imports the heapq module

# Define a simple weighted graph for Prim's algorithm
def create_graph_prim():
    G = nx.Graph()
    edges = [('A', 'B', 4), ('A', 'H', 8), ('B', 'C', 8),
             ('B', 'H', 11), ('C', 'D', 7), ('C', 'F', 4),
             ('C', 'I', 2), ('D', 'E', 9), ('D', 'F', 14),
             ('E', 'F', 10), ('F', 'G', 2), ('G', 'H', 1),
             ('G', 'I', 6), ('H', 'I', 7)]
    G.add_weighted_edges_from(edges)
    return G

# Prim's algorithm with visualization
def prim(G, start, plot=False):
    mst = nx.Graph()
    visited = {start}
    edges = [(data['weight'], u, v) for u, v, data in G.edges(data=True) if u == start or v == start]
    heapify(edges)  # No prefix needed
    
    if plot:
        plot_graph(G, "Initial Graph with Weights", highlight_edges=None)
        st.pyplot(plt)

    while edges:
        weight, u, v = heappop(edges)  # No prefix needed
        if v not in visited:
            visited.add(v)
            mst.add_edge(u, v, weight=weight)
            for next_edge in G.edges(v, data=True):
                if next_edge[1] not in visited:
                    heappush(edges, (next_edge[2]['weight'], v, next_edge[1]))  # No prefix needed
            if plot:
                plot_graph(G, "Prim's Algorithm Step-by-Step", highlight_edges=mst.edges())
                st.pyplot(plt)
    return mst

# Plotting function with optional edge highlighting
def plot_graph(G, title, highlight_edges):
    pos = nx.spring_layout(G, scale=2)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    if highlight_edges:
        nx.draw_networkx_edges(G, pos, edgelist=highlight_edges, edge_color='red', width=2)
    plt.title(title)

# Streamlit interface
def main():
    st.title("Prim's Algorithm Demonstration")
    G_prim = create_graph_prim()
    start_node = st.selectbox("Choose start node", list(G_prim.nodes()))
    
    if st.button("Compute MST with Prim"):
        prim(G_prim, start_node, plot=True)

if __name__ == "__main__":
    main()
