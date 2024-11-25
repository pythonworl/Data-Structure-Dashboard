import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

# Define a simple weighted graph
def create_graph_mdg():
    G = nx.Graph()
    edges = [('A', 'B', 3), ('A', 'C', 1), ('B', 'C', 7),
             ('B', 'D', 5), ('B', 'E', 1), ('C', 'E', 2),
             ('D', 'E', 7), ('D', 'F', 6), ('E', 'F', 8),
             ('E', 'G', 9), ('F', 'G', 11)]
    G.add_weighted_edges_from(edges)
    return G

# Minimum Degree Greedy algorithm
def mdg(G, plot=False):
    mst = nx.Graph()
    nodes = set(G.nodes())
    selected_nodes = set()

    # Initially, pick any node to start
    start_node = list(nodes)[0]
    selected_nodes.add(start_node)
    
    if plot:
        plot_graph(G, "Initial Graph with Weights", mst)
        st.pyplot(plt)

    while selected_nodes != nodes:
        min_edge = None
        for node in selected_nodes:
            for neighbor, data in G[node].items():
                if neighbor not in selected_nodes:
                    if min_edge is None or data['weight'] < min_edge[2]['weight']:
                        min_edge = (node, neighbor, data)
        
        if min_edge:
            u, v, data = min_edge
            mst.add_edge(u, v, weight=data['weight'])
            selected_nodes.add(v)
            if plot:
                plot_graph(G, "MDG Algorithm Step-by-Step", mst)
                st.pyplot(plt)

    return mst

# Plotting function with optional MST highlighting
def plot_graph(G, title, mst):
    pos = nx.spring_layout(G, scale=2)
    plt.figure(figsize=(10, 8))
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=700, edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})
    if mst.edges():
        nx.draw_networkx_edges(G, pos, edgelist=mst.edges(), edge_color='red', width=2)
    plt.title(title)

# Streamlit interface
def main():
    st.title("MDG Algorithm Demonstration")
    G_mdg = create_graph_mdg()
    
    if st.button("Compute MST with MDG"):
        mdg(G_mdg, plot=True)

if __name__ == "__main__":
    main()
