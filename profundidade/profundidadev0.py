def busca_em_profundidade(grafo, inicio):
    visitado, pilha = set(), [inicio]
    ordem_visita = []  
    while pilha:
        vertice = pilha.pop()
        if vertice not in visitado:
            visitado.add(vertice)
            ordem_visita.append(vertice) 
            
            pilha.extend(vizinho for vizinho in grafo[vertice] if vizinho not in visitado)
    return ordem_visita


def criar_grafo():
    vertices = input("Digite os vértices separados por vírgula (ex: A,B,C,D,E,F): ").split(',')
    grafo = {}
    for vertice in vertices:
        conexoes = input(f"Digite as conexões do vértice {vertice} separadas por vírgula (ex: A,B,C): ").split(',')
        grafo[vertice] = set(conexoes)
    return grafo


grafo = criar_grafo()
vertice_inicial = input("Digite o vértice inicial: ")

print("Ordem de visita dos vértices:")
print(busca_em_profundidade(grafo, vertice_inicial)) 
