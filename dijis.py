import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import heapq

# Define a simple undirected weighted graph
def create_graph():
    G = nx.Graph()
    edges = [('A', 'B', 1), ('A', 'C', 4), ('B', 'C', 2), 
             ('B', 'D', 5), ('C', 'D', 1), ('D', 'E', 3)]
    G.add_weighted_edges_from(edges)
    return G

# Dijkstra's algorithm with visualization
def dijkstra(G, start, plot=False):
    distances = {node: float('infinity') for node in G}
    distances[start] = 0
    priority_queue = [(0, start)]
    path = {}

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Plot the current state of the graph
        if plot:
            plot_graph(G, distances, path, current_node)
            st.pyplot(plt)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in G[current_node].items():
            distance = current_distance + weight['weight']

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                path[neighbor] = current_node

    return distances, path

# Improved plotting function to avoid label collision
def plot_graph(G, distances, path, current_node):
    pos = nx.spring_layout(G, scale=2)  # Increase the scale for better spacing
    plt.figure(figsize=(12, 10))
    nx.draw(G, pos, with_labels=False, node_size=700, node_color='skyblue', edge_color='gray')
    nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): d['weight'] for u, v, d in G.edges(data=True)})

    # Draw the current node in red
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color='red')
    
    # Custom labels for nodes to avoid overlap
    labels = {node: f"{node}\n{dist if dist != float('infinity') else '∞'}" for node, dist in distances.items()}
    nx.draw_networkx_labels(G, pos, labels=labels, font_size=10)

# Streamlit interface
def main():
    st.title("Dijkstra's Algorithm Demonstration")
    G = create_graph()
    start_node = st.selectbox("Choose start node", list(G.nodes()))
    if st.button("Compute Shortest Paths"):
        distances, path = dijkstra(G, start_node, plot=True)
        st.write("Shortest distances from node:", distances)
        st.write("Paths:", path)

if __name__ == "__main__":
    main()
