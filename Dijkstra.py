from grafo import *
import matplotlib.pyplot as plt
import networkx as nx


if __name__ == "__main__":
    grafo = Grafo()
    vrts = ['A', 'B', 'C', 'D', 'E','F','G']

    for vertice in vrts :
        grafo.adicionar_vertice(vertice)

    grafo.adicionar_aresta("A", "B",8)
    grafo.adicionar_aresta("A", "C",3)
    grafo.adicionar_aresta("A", "D",12)
    grafo.adicionar_aresta("A", "E", 4)
    grafo.adicionar_aresta("A", "F", 5)
    grafo.adicionar_aresta("A", "G", 14)

    grafo.adicionar_aresta("B", "C",2)
    grafo.adicionar_aresta("B", "D",9)
    grafo.adicionar_aresta("B", "E", 1)
    grafo.adicionar_aresta("B", "F", 6)
    grafo.adicionar_aresta("B", "G", 1)

    grafo.adicionar_aresta("C", "D", 7)
    grafo.adicionar_aresta("C", "E",9)
    grafo.adicionar_aresta("C", "F", 14)
    grafo.adicionar_aresta("C", "G", 2)

    grafo.adicionar_aresta("D", "E",10)
    grafo.adicionar_aresta("D", "G",6)
    grafo.adicionar_aresta("D", "F",3)

    grafo.adicionar_aresta("E", "F",15)
    grafo.adicionar_aresta("E", "G",13)

    grafo.adicionar_aresta("F", "G",4)

    origem = "B"
    destino = "G"
    caminho, peso_total = grafo.dijkstra_com_menor_peso(origem, destino)

    G = nx.DiGraph()
    for vertice in grafo.lista_vertices:
        G.add_node(vertice)

    for vertice, lista_arestas in grafo.lista_vertices.items():
        temp = lista_arestas.cabeca
        while temp:
            G.add_edge(vertice, temp.valor, weight=temp.peso)
            temp = temp.prox

    pos = {
        'A': (2.150, 1.835),
        'B': (3.841, 2.110),
        'C': (5.223, 2.110),
        'D': (3.841, 1.654),
        'E': (7.5, 1.713),
        'F': (8, 2),
        'G': (5.223, 1.854),
    }

    edge_colors = {}

    if caminho:
        caminho_edges = [(caminho[i], caminho[i + 1]) for i in range(len(caminho) - 1)]

        for u, v in caminho_edges:
            edge_colors[(u, v)] = 'r'

    plt.figure(figsize=(10, 8))

    edges = G.edges(data=True)
    labels = nx.get_edge_attributes(G, 'weight')

    edge_color_list = [edge_colors.get(edge, 'gray') for edge in G.edges()]

    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, font_size=13, font_weight='bold',
            edge_color=edge_color_list, width=2)

    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=13)

    if caminho:
        caminho_menor = ', '.join(caminho)
    else:
        caminho_menor = "Caminho Impossível"

    plt.text(6, 2.1, f'Caminho Percorrido: {caminho_menor} \nPeso Total: {peso_total} ', fontsize=12, ha='left',
             color='black')

    plt.title("Grafo com Menor Peso Destacado", fontsize=14)
    plt.axis('off')
    plt.show()