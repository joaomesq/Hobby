from collections import deque

def bfs(grafo, no_inicial):
    # Conjunto para rastrear os nós já visitados
    visitados = set()
    # Fila que dita a ordem de exploração (FIFO)
    fila = deque([no_inicial])
    
    # Marca o nó inicial como visitado
    visitados.add(no_inicial)
    
    print("Ordem de visitação do BFS:")
    
    while fila:
        # Remove e retorna o nó mais antigo da fila
        no_atual = fila.popleft()
        print(no_atual, end=" ")
        
        # Verifica todos os vizinhos do nó atual
        for vizinho in grafo[no_atual]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                fila.append(vizinho)

# Representação do Grafo por Lista de Adjacência
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Executa o algoritmo partindo do nó 'A'
bfs(grafo, 'A')
