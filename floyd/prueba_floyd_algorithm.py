"""
────────────────────────────────────────────────────────────────────────────────
─██████████████─██████─────────██████████████─████████──████████─████████████───
─██░░░░░░░░░░██─██░░██─────────██░░░░░░░░░░██─██░░░░██──██░░░░██─██░░░░░░░░████─
─██░░██████████─██░░██─────────██░░██████░░██─████░░██──██░░████─██░░████░░░░██─
─██░░██─────────██░░██─────────██░░██──██░░██───██░░░░██░░░░██───██░░██──██░░██─
─██░░██████████─██░░██─────────██░░██──██░░██───████░░░░░░████───██░░██──██░░██─
─██░░░░░░░░░░██─██░░██─────────██░░██──██░░██─────████░░████─────██░░██──██░░██─
─██░░██████████─██░░██─────────██░░██──██░░██───────██░░██───────██░░██──██░░██─
─██░░██─────────██░░██─────────██░░██──██░░██───────██░░██───────██░░██──██░░██─
─██░░██─────────██░░██████████─██░░██████░░██───────██░░██───────██░░████░░░░██─
─██░░██─────────██░░░░░░░░░░██─██░░░░░░░░░░██───────██░░██───────██░░░░░░░░████─
─██████─────────██████████████─██████████████───────██████───────████████████───
────────────────────────────────────────────────────────────────────────────────
1. inicializar variables, initialize(n)
2. agregar nodos, addEdge(u, v, w)
3. la distancia entre u -> v será d[u][v]
   el path entre u -> v esta en el array getPath(u,v)

"""
import pandas as pd
MX = 500
INF = 1e18

d = []
parent = []

for f in range(MX):
	d.append([])
	parent.append([])
	for c in range(MX):
		d[f].append(None)
		parent[f].append(None)

def initialize(n):
	# n = #nodos 

	for i in range(n):
		for j in range(n):
			d[i][j] = INF
			parent[i][j] = -1
		d[i][i] = 0


def addEdge(u, v, w):
	# u = nodo1, v = nodo2, w = distancia entre nodo1 y nodo2
	# los nodos deben estar numerados de 1 .. n

	u = u - 1 
	v = v - 1
	d[u][v] = min(d[u][v], w) 
	d[v][u] = min(d[v][u], w)
	parent[u][v] = u 
	parent[v][u] = v


def floydWarshall(n):
	# n = #nodos

	for k in range(n):
		for u in range(n):
			for v in range(n):
				if d[u][k] == INF: 
					continue
				if d[k][v] == INF: 
					continue
				if d[u][k] + d[k][v] < d[u][v]:
					d[u][v] = d[u][k] + d[k][v]
					parent[u][v] = parent[k][v]


def getPath(u,v):
    # u = nodo1, v = nodo2
	# los nodos deben estar numerados de 1 .. n

	u = u - 1
	v = v - 1

	if d[u][v] == INF:
		return ' '
	path = []

	while v != -1: 
		path.append(v + 1)
		v = parent[u][v]

	path.reverse()
	return path

def main():
	initialize(4)
	
	addEdge(1, 2, 5)
	addEdge(2, 4, 8)
	addEdge(1, 3, 3)
	addEdge(3, 4, 6)

	floydWarshall(4)
	print(getPath(1,4))

if __name__ == "__main__":
    main()
