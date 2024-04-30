#Por Juan David Obando Novoa y Alejandro Mariscal 

from sys import stdin
from typing import Counter
from Eulerpath import Graph
import sys 
import heapq
sys.setrecursionlimit(2000) 


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
        lista=buscarFundamentales(compuestos_fund)
        if lista:
            print(calc(lista, w1, w2))
        else:
            print("No se puede")

        
def buscarFundamentales(lista, solucion_parcial=None):
    if solucion_parcial is None:
        solucion_parcial = []

    if not lista:
        return solucion_parcial

    if solucion_parcial:
        inicio = solucion_parcial[-1][1]
    else:
        ocurrencias = Counter([x for (x,y) in lista] + [y for (x,y) in lista])
        impares = [k for k in ocurrencias if ocurrencias[k] % 2]
        inicio = impares[0] if impares else lista[0][0]

    for indice, (x, y) in enumerate(lista):
        if x == inicio:
            resultado = buscarFundamentales(lista[:indice] + lista[indice+1:], solucion_parcial + [(x, y)])
            if resultado:
                return resultado
        elif y == inicio:
            resultado = buscarFundamentales(lista[:indice] + lista[indice+1:], solucion_parcial + [(y, x)])
            if resultado:
                return resultado

    return False


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
