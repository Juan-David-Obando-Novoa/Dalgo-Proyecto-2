def ltp(W1, w2, m1, m2, c1, c2):
    if c1 == c2:
        return 1+abs(abs(m1)-abs(m2))%W1 
    if c1 != c2:
        return w2-abs(abs(m1)-abs(m2))%w2


print(ltp(3,5,1,9,"positivo","negativa"))
import heapq

def dijkstra(graph, start, end):
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    previous_nodes = {node: None for node in graph}
    queue = [(0, start)]

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                heapq.heappush(queue, (distance, neighbor))

    path = []
    while end:
        path.append(end)
        end = previous_nodes[end]
    path.reverse()

    return distances, path



adj_list = {-6: {3: 3, 1: 8},
    3: {7: 3},
    1: {-6: 8},
    7: {7: 5, -6: 6, 3: 2}}


#print(dijkstra(adj_list, -6))
def calcular_distancias(grafo, w1, w2):
    distancias = {}
    for nodo_inicio in grafo:
        distancias[nodo_inicio] = {}
        for nodo_fin in grafo:
            if nodo_inicio != nodo_fin:
                m1 = nodo_inicio
                m2 = nodo_fin
                c1 = 'positivo' if m1 > 0 else 'negativo'
                c2 = 'positivo' if m2 > 0 else 'negativo'
                if abs(m1) == abs(m2):  # Si los valores absolutos son iguales
                    distancias[nodo_inicio][nodo_fin] = 1000  # Establece la distancia a 1000
                else:
                    distancias[nodo_inicio][nodo_fin] = ltp(w1, w2, m1, m2, c1, c2)
    return distancias
#  return 1+abs(m1-m2)%W1 
#     if c1 != c2:
#         return w2-abs(m1-m2)%w2
lista = [[-6, 3], [3, 1], [1, 7]]
diccionario = {}

for par in lista:
    for valor in par:
        diccionario[valor] = None
        diccionario[-valor] = None



diccionario= calcular_distancias(diccionario, 3,5)
print(diccionario)
distances, path = dijkstra(diccionario, 1, -1)
print(distances)  # Debería imprimir las distancias más cortas desde 5 hasta cada nodo
print(path)  # Debería imprimir la ruta más corta desde 5 hasta -5
distances, path = dijkstra(diccionario, 1, -1)
print("Costo total:", distances[-1])  # Imprime el costo total del camino más corto desde 1 hasta -1
print(ltp(3, 5, 1, 3, "positivo", "positivo"))
print(ltp(3, 5, 3, -7, "positivo", "negativo"))
print(ltp(3, 5, -7, -1, "negativo", "negativo"))


print(ltp(3, 5, 1, 3, "positivo", "positivo"))
print(ltp(3, 5, 3, -7, "positivo", "negativo"))
print(ltp(3, 5, -7, -1, "negativo", "negativo"))