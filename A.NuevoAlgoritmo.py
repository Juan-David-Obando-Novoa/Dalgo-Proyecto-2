from sys import stdin
from typing import Counter
from Eulerpath import Graph
import sys 
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

        print(compuestos_fund)

        compuestos_fund = list(set(tuple(sorted(i)) for i in compuestos_fund))

        matriz= crearmatrizAdyacencia(compuestos_fund)
        print(encontrarFundamentales(compuestos_fund))

        
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



if __name__ == "__main__":
    main()
