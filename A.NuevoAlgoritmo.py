from sys import stdin
from typing import Counter
from Eulerpath import Graph
import sys 
import heapq
sys.setrecursionlimit(2000) 


def matriz_lista(matriz):
    lista =[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                lista.append([i,j])
    return lista



def main():
    case_number = int(stdin.readline().strip())
    for _ in range(case_number):
        line = list(map(int, stdin.readline().strip().split()))
        w1=line[1]
        w2= line[2]
        compuestos_fund= []
        g1 = Graph(line[0])

        for t in range(line[0]):
            comp = list(map(int, stdin.readline().strip().split()))
            #g1.addEdge(comp[0], comp[1])
            compuestos_fund.append(comp)
        compuestos_fund = [comp for comp in compuestos_fund if comp]

        compuestos_fund = list(set(tuple(sorted(i)) for i in compuestos_fund))

        matriz= crearmatrizAdyacencia(compuestos_fund)
        lista=encontrarFundamentales(compuestos_fund)
        if lista:
            print(calc(lista, w1, w2))
        else:
            print("No se puede")

        
def encontrarFundamentales(l):
    stack = [(l, [])]  # Initialize stack with initial parameters
    
    while stack:
        l, partial = stack.pop()  # Pop the parameters from stack
        
        # If list of tuple we need to order is empty, then we have finished
        if l == []:
            return partial
        
        # Otherwise, we need to try to continue our partial solution
        # with tuples (in any order)
        
        # Where to start:
        if len(partial):
            start = partial[-1][1]  # Start with last element in partial solution if any
        else:
            # Start chain with odd occurrence number
            occ = Counter([x for (x,y) in l] + [y for (x,y) in l])
            odd = [k for k in occ if occ[k] % 2]
            if len(odd) > 0:
                start = odd[0]
            else:
                # All numbers appear an even number of times: we can start wherever
                # we want, there is a solution starting from everywhere
                start = l[0][0]
        
        # Iterate through the list of tuples
        for i, (x, y) in enumerate(l):
            # Try to add (x,y) to our partial solution
            if x == start:
                # Add the next parameters to the stack
                stack.append((l[:i] + l[i+1:], partial + [(x, y)]))
            elif y == start:
                # Add the next parameters to the stack
                stack.append((l[:i] + l[i+1:], partial + [(y, x)]))
    return False




def crearmatrizAdyacencia(compuestos_fund):
    n = len(compuestos_fund)
    matrizAdyacencia = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):  # Comienza desde i+1 para evitar conexiones bidireccionales
            if len(compuestos_fund[i]) >= 2 and len(compuestos_fund[j]) >= 2:
                if (compuestos_fund[i][0] == compuestos_fund[j][0] or compuestos_fund[i][1] == compuestos_fund[j][1] or compuestos_fund[i][1] == compuestos_fund[j][0] or compuestos_fund[i][0] == compuestos_fund[j][1]):
                    matrizAdyacencia[i][j] = 1
    return matrizAdyacencia

def ltp(W1, w2, m1, m2, c1, c2):
    if c1 == c2:
        return 1+abs(abs(m1)-abs(m2))%W1 
    if c1 != c2:
        return w2-abs(abs(m1)-abs(m2))%w2
    

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



if __name__ == "__main__":
    main()
