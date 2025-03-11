import heapq
import itertools


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        self.peso = 0


class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar_node(self, valor, peso=0):
        novo_node = Node(valor)
        novo_node.peso = peso

        if not self.cabeca:
            self.cabeca = novo_node
            return

        ultimo = self.cabeca
        while ultimo.prox:
            ultimo = ultimo.prox

        ultimo.prox = novo_node

    def obter_peso(self, valor):
        temp = self.cabeca
        while temp:
            if temp.valor == valor:
                return temp.peso
            temp = temp.prox
        return None

    def get_nodes(self):
        nodes = []
        temp = self.cabeca
        while temp:
            nodes.append(temp)
            temp = temp.prox
        return nodes

    def display(self):
        temp = self.cabeca
        while temp:
            if temp.prox:
                print(f'{temp.valor} [{temp.peso}]', end=' -> ')
            else:
                print(f'{temp.valor} [{temp.peso}]', end='')
            temp = temp.prox


class Grafo:
    def __init__(self):
        self.lista_vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_vertices:
            self.lista_vertices[vertice] = ListaEncadeada()

    def adicionar_aresta(self, v1, v2, peso=0):
        if v1 in self.lista_vertices and v2 in self.lista_vertices:
            self.lista_vertices[v1].adicionar_node(v2, peso)

    def exibir_grafo(self):
        for chave, valor in self.lista_vertices.items():
            print(f'Vértice: [{chave}] Arestas: ', end='')
            valor.display()

    def calcular_peso_caminho(self, caminho):
        peso_total = 0
        for i in range(len(caminho) - 1):
            peso = self.lista_vertices[caminho[i]].obter_peso(caminho[i + 1])
            if peso is None:
                return float('inf')
            peso_total += peso
        return peso_total

    def resolver_tsp(self, origem):
        vertices = list(self.lista_vertices.keys())
        vertices.remove(origem)

        min_peso = float('inf')
        melhor_caminho = []

        for permutacao in itertools.permutations(vertices):
            caminho = [origem] + list(permutacao) + [origem]
            peso_caminho = self.calcular_peso_caminho(caminho)


            if peso_caminho < min_peso:
                min_peso = peso_caminho
                melhor_caminho = caminho

        return melhor_caminho, min_peso

    def dijkstra_com_menor_peso(self, origem, destino):
        pq = [(0, origem, [])]
        distancias = {v: float('inf') for v in self.lista_vertices}
        distancias[origem] = 0
        vertices_visitados = set()

        while pq:
            peso_acumulado, ver_atual, caminho_atual = heapq.heappop(pq)

            if ver_atual in vertices_visitados:
                continue

            vertices_visitados.add(ver_atual)
            caminho_atual = caminho_atual + [ver_atual]

            if ver_atual == destino:
                return caminho_atual, peso_acumulado

            temp = self.lista_vertices[ver_atual].cabeca
            while temp:
                novo_peso = peso_acumulado + temp.peso

                if novo_peso < distancias[temp.valor]:
                    distancias[temp.valor] = novo_peso
                    heapq.heappush(pq, (novo_peso, temp.valor, caminho_atual))

                temp = temp.prox

        return None, float('inf')

