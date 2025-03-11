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

    def dfs_tsp(self, inicio):
        vertices = list(self.lista_vertices.keys())
        vertices.remove(inicio)

        melhor_caminho = None
        menor_peso = float('inf')


        def dfs(caminho_atual, vertices_restantes, peso_atual):
            nonlocal melhor_caminho, menor_peso

            if not vertices_restantes:
                peso_atual += self.obter_peso_aresta(caminho_atual[-1], caminho_atual[0])

                if peso_atual < menor_peso:
                    menor_peso = peso_atual
                    melhor_caminho = caminho_atual + [caminho_atual[0]]
                return

            for v in vertices_restantes:
                novo_caminho = caminho_atual + [v]
                novos_vertices_restantes = vertices_restantes.copy()
                novos_vertices_restantes.remove(v)

                novo_peso = peso_atual + self.obter_peso_aresta(caminho_atual[-1], v)

                dfs(novo_caminho, novos_vertices_restantes, novo_peso)

        dfs([inicio], vertices, 0)

        return melhor_caminho, menor_peso

    def obter_peso_aresta(self, v1, v2):

        temp = self.lista_vertices[v1].cabeca
        while temp:
            if temp.valor == v2:
                return temp.peso
            temp = temp.prox
        return float('inf')
