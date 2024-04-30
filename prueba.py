def ltp(W1, w2, m1, m2, c1, c2):
    if c1 == c2:
        return 1+abs(abs(m1)-abs(m2))%W1 
    if c1 != c2:
        return w2-abs(abs(m1)-abs(m2))%w2


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
lista = [(-6, 3), (3, 1), (1, 7)]

def calc(lista, w1, w2):

    diccionario = {}

    for par in lista:
        for valor in par:
            diccionario[valor] = None
            diccionario[-valor] = None



    diccionario= calcular_distancias(diccionario, w1,w2)
    suma=0
    mensaje=""

    for i in range(0,len(lista)-1):
        valor=lista[i][1]
        llegada=-valor
        distances, path = dijkstra(diccionario, valor, llegada)
        suma+=distances[llegada]  # Debería imprimir las distancias más cortas desde 5 hasta cada nodo
        mensaje+=str(lista[i])+", "
        for j in range(1,len(path)):
            mensaje+=str(path[j])+", "
    mensaje+=str(lista[-1])+" "+str(suma)
    return mensaje

print(calc(lista,3,5))