from queue import Queue


class Node:
    def __init__(self, valor):
        self.valor = valor
        self.prox = None
        self.peso = 0

class ListaEncadeada:
    def __init__(self):
        self.cabeca = None

    def adicionar_node(self, valor,peso=0):
        novo_node = Node(valor)
        novo_node.peso = peso

        if not self.cabeca:
            self.cabeca = novo_node
            return

        ultimo = self.cabeca
        while ultimo.prox:
            ultimo = ultimo.prox

        ultimo.prox = novo_node

    def remover_primeiro(self):
        if self.cabeca:
            removido = self.cabeca
            self.cabeca = self.cabeca.prox
            return removido.valor
        return None

    def display(self):
        temp = self.cabeca
        while temp:
            if temp.prox:
                print(f'{temp.valor} [{temp.peso}]', end=' -> ')
            else:
                print(f'{temp.valor} [{temp.peso}]', end='')
            temp = temp.prox
        print('')


class Grafo:
    def __init__(self):
        self.lista_vertices = {}

    def adicionar_vertice(self, vertice):
        if vertice not in self.lista_vertices:
            self.lista_vertices[vertice] = ListaEncadeada()

    def adicionar_aresta(self, v1, v2,peso=0):
        if v1 in self.lista_vertices and v2 in self.lista_vertices:
            self.lista_vertices[v1].adicionar_node(v2,peso)

    def exibir_grafo(self):
        for chave, valor in self.lista_vertices.items():
            print(f'Vértice: [{chave}] Arestas: ', end='')
            valor.display()

    def bfs(self, origem, destino):
        fila = Queue()
        vertices_visitados = {}

        fila.put(origem)
        vertices_visitados[origem] = None

        saltos = 0

        while not fila.empty():
            num_novos_vizinhos = fila.qsize()
            saltos += 1

            for _ in range(num_novos_vizinhos):
                ver_atual = fila.get()

                if ver_atual == destino:
                    caminho_atual = []
                    while ver_atual is not None:
                        caminho_atual.append(ver_atual)
                        ver_atual = vertices_visitados[ver_atual]

                    caminho_atual.reverse()
                    return saltos, caminho_atual

                temp = self.lista_vertices[ver_atual].cabeca

                while temp:
                    if temp.valor not in vertices_visitados:
                        vertices_visitados[temp.valor] = ver_atual
                        fila.put(temp.valor)

                    temp = temp.prox

        return None

    def dfs_com_menor_peso(self, origem, destino):
        pilha = [(origem, 0, [])]
        vertices_visitados = set()

        menor_peso = float('inf')
        melhor_caminho = None

        while pilha:
            ver_atual, peso_acumulado, caminho_atual = pilha.pop()
            caminho_atual = caminho_atual + [ver_atual]

            if ver_atual == destino:

                if peso_acumulado < menor_peso:
                    menor_peso = peso_acumulado
                    melhor_caminho = caminho_atual
                continue

            if ver_atual not in vertices_visitados:
                vertices_visitados.add(ver_atual)

                temp = self.lista_vertices[ver_atual].cabeca
                while temp:
                    if temp.valor not in vertices_visitados:
                        pilha.append((temp.valor, peso_acumulado + temp.peso, caminho_atual))

                    temp = temp.prox

        return melhor_caminho, menor_peso

