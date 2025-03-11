from grafo import *
import matplotlib.pyplot as plt
import networkx as nx

if __name__ == "__main__":
    grafo = Grafo()
    vrts = ['A', 'B', 'C', 'D', 'E']

    for vertice in vrts:
        grafo.adicionar_vertice(vertice)

    grafo.adicionar_aresta('A', 'B', 10)
    grafo.adicionar_aresta('A', 'C', 15)
    grafo.adicionar_aresta('A', 'D', 20)
    grafo.adicionar_aresta('A', 'E', 25)
    grafo.adicionar_aresta('B', 'A', 10)
    grafo.adicionar_aresta('B', 'C', 35)
    grafo.adicionar_aresta('B', 'D', 30)
    grafo.adicionar_aresta('B', 'E', 40)
    grafo.adicionar_aresta('C', 'A', 15)
    grafo.adicionar_aresta('C', 'B', 35)
    grafo.adicionar_aresta('C', 'D', 30)
    grafo.adicionar_aresta('C', 'E', 45)
    grafo.adicionar_aresta('D', 'E', 50)
    grafo.adicionar_aresta('D', 'C', 30)
    grafo.adicionar_aresta('D', 'A', 20)
    grafo.adicionar_aresta('D', 'C', 30)
    grafo.adicionar_aresta('E', 'A', 25)
    grafo.adicionar_aresta('E', 'B', 40)
    grafo.adicionar_aresta('E', 'C', 45)
    grafo.adicionar_aresta('E', 'D', 50)

    caminho, custo_total = grafo.dfs_tsp('D')

    print(f"Caminho do TSP: {caminho}")
    print(f"Custo Total: {custo_total}")

    G = nx.Graph()
    for vertice in grafo.lista_vertices:
        G.add_node(vertice)

    for vertice, lista_arestas in grafo.lista_vertices.items():
        for node in lista_arestas.get_nodes():
            G.add_edge(vertice, node.valor, weight=node.peso)

    pos = {
        'A': (0, 2),
        'B': (3, 2),
        'C': (5, 2.1),
        'D': (3, 1.54),
        'E': (5, 1.9),
    }

    edge_colors = {}
    if caminho:
        caminho_edges = [(min(caminho[i], caminho[i + 1]), max(caminho[i], caminho[i + 1])) for i in
                         range(len(caminho) - 1)]
        for u, v in caminho_edges:
            edge_colors[(u, v)] = 'r'

    plt.figure(figsize=(10, 8))
    edge_color_list = [edge_colors.get((min(u, v), max(u, v)), 'gray') for u, v in G.edges()]

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=13, font_weight='bold',
            edge_color=edge_color_list, width=2)

    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=13)

    if caminho:
        caminho_menor = ', '.join(caminho)
    else:
        caminho_menor = "Caminho Impossível"

    plt.text(0, 2.1, f'Caminho Percorrido: {caminho_menor} \nPeso Total: {custo_total}', fontsize=12, ha='left',
             color='black')

    plt.title("Grafo com Menor Caminho Percorrido (Caixeiro Viajante)", fontsize=14)
    plt.axis('off')
    plt.show()
