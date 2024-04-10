def busca_em_profundidade(grafo, raiz):
    visitados = set()  
    pilha = [raiz]     
    while pilha:
        vertice_atual = pilha[-1]  
        vizinhos_nao_visitados = [vizinho for vizinho in grafo[vertice_atual] if vizinho not in visitados]
        if vizinhos_nao_visitados:
            proximo_vertice = vizinhos_nao_visitados[0]
            print("Visitando vértice:", proximo_vertice)
            visitados.add(proximo_vertice)
            pilha.append(proximo_vertice)
        else:
            pilha.pop()

grafo = {}
vertices = input("Insira todos os vértices separados por vírgula: ").split(',')

for vertice in vertices:
    conexoes = input(f"Insira as conexões para o vértice {vertice}: ").split(',')
    grafo[vertice] = conexoes

raiz = input("Escolha o vértice inicial para a busca: ")

print("Busca em Profundidade:")
busca_em_profundidade(grafo, raiz)
