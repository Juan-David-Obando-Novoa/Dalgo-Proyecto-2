from sys import stdin
from Eulerpath import Graph
import sys 
sys.setrecursionlimit(2000) 


# Create a graph given in the above diagram
def crearmatrizAdyacencia(compuestos_fund):
    n = len(compuestos_fund)
    matrizAdyacencia = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(i+1, n):  # Comienza desde i+1 para evitar conexiones bidireccionales
            if (compuestos_fund[i][0] == compuestos_fund[j][0] or compuestos_fund[i][1] == compuestos_fund[j][1] or compuestos_fund[i][1] == compuestos_fund[j][0] or compuestos_fund[i][0] == compuestos_fund[j][1]) and sum(matrizAdyacencia[i]) < 2:
                matrizAdyacencia[i][j] = 1
    return matrizAdyacencia

def matriz_lista(matriz):
    lista =[]
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == 1:
                lista.append([i,j])
    return lista

def has_eulerian_path(matrizAdyacencia):
    # Contar vértices con grado impar
    odd = [sum(i)%2 for i in matrizAdyacencia].count(1)
    return odd == 0 or odd == 2

def dfs(node, visited, matrizAdyacencia):
    visited[node] = True
    for i, val in enumerate(matrizAdyacencia[node]):
        if val == 1 and not visited[i]:
            dfs(i, visited, matrizAdyacencia)

def is_connected(matrizAdyacencia):
    visited = [False] * len(matrizAdyacencia)
    dfs(0, visited, matrizAdyacencia)
    return all(visited)

def crearListaSinALibres(compuestos_fund, grafo):
    listaNueva=[]
    for fila in range(len(grafo)):
        grafo[fila][0]
        listaNueva.append(compuestos_fund[grafo[fila][0]])
        if fila ==len(grafo)-1:
            listaNueva.append(compuestos_fund[grafo[fila][1]])
        while len(listaNueva) > len(compuestos_fund):
            listaNueva.pop()
    return listaNueva

def ajustarLista(grafo):
    for i in range(len(grafo)):
        for j in range(i+1, len(grafo)):
            if grafo[i][1] == grafo[j][1]:
                grafo[j] = [grafo[j][1], grafo[j][0]]
    return grafo

#------------------------------------------------------------------------------------------------------------------------------------------------------------------------


    

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
        matriz= crearmatrizAdyacencia(compuestos_fund)
        if is_connected(matriz):
            has_eulerian_path(matriz)
            lista = matriz_lista(matriz)
            for conexion in lista:
                g1.addEdge(conexion[0], conexion[1])

            g1.printEulerTour()
            grafo= g1.lista 

            ListaSinALibres= crearListaSinALibres(compuestos_fund, grafo)
            ListaSinALibres  = ajustarLista(ListaSinALibres)
            print(ListaSinALibres)
        else:
            print("No se puede")



if __name__ == "__main__":
    main()
