from grafo import *
import matplotlib.pyplot as plt
import networkx as nx


if __name__ == "__main__":
    grafo = Grafo()
    grafo.adicionar_vertice("A")
    grafo.adicionar_vertice("B")
    grafo.adicionar_vertice("C")
    grafo.adicionar_vertice("D")
    grafo.adicionar_vertice("E")
    grafo.adicionar_vertice("F")
    grafo.adicionar_vertice("G")
    grafo.adicionar_vertice("H")
    grafo.adicionar_vertice("I")
    grafo.adicionar_vertice("J")
    grafo.adicionar_vertice("K")
    grafo.adicionar_vertice("L")
    grafo.adicionar_vertice("M")

    grafo.adicionar_aresta("A", "B",10)
    grafo.adicionar_aresta("A", "C",5)
    grafo.adicionar_aresta("A", "D",1)

    grafo.adicionar_aresta("B", "C",3)
    grafo.adicionar_aresta("B", "E",10)

    grafo.adicionar_aresta("C", "F",10)

    grafo.adicionar_aresta("D", "E",2)
    grafo.adicionar_aresta("D", "G",2)
    grafo.adicionar_aresta("D", "M",1)

    grafo.adicionar_aresta("E", "F",1)
    grafo.adicionar_aresta("E", "H",10)

    grafo.adicionar_aresta("F", "I",10)

    grafo.adicionar_aresta("G", "H",3)

    grafo.adicionar_aresta("H", "I",1)

    grafo.adicionar_aresta("I", "J",10)

    grafo.adicionar_aresta("J", "K",10)

    grafo.adicionar_aresta("K", "L",10)

    grafo.adicionar_aresta("L", "M",10)

    origem = "A"
    destino = "I"
    caminho, peso_total = grafo.dfs_com_menor_peso(origem, destino)

    G = nx.DiGraph()
    for vertice in grafo.lista_vertices:
        G.add_node(vertice)

    for vertice, lista_arestas in grafo.lista_vertices.items():
        temp = lista_arestas.cabeca
        while temp:
            G.add_edge(vertice, temp.valor, weight=temp.peso)
            temp = temp.prox

    pos = {
        'A': (0, 2),
        'B': (3, 2),
        'C': (5, 2.1),
        'D': (3, 1.54),
        'E': (5, 1.9),
        'F': (7.5, 2.1),
        'G': (5.57, 1.667),
        'H': (7.5, 1.75),
        'I': (7.5, 1.9),
        'J': (10.5, 1.9),
        'K': (13.5, 1.9),
        'L': (16.5, 1.9),
        'M': (19.5, 1.9),
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

    plt.text(8.7, 2.1, f'Caminho Percorrido: {caminho_menor} \nPeso Total: {peso_total} ', fontsize=12, ha='left',
             color='black')

    plt.title("Grafo com Menor Peso Destacado", fontsize=14)
    plt.axis('off')
    plt.show()