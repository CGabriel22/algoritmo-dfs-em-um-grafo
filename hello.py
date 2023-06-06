vertices_amount, edges_amount, mark = 0, 0, 0
graph_type = "D"
vertices_list, edges_list, adjacency_list, color, d, f = [], [], [], [], [], []

class GraphHasNoDirectionException(Exception):
  pass

def readFile():
  global vertices_amount, edges_amount, graph_type, vertices_list, edges_list, adjacency_list
  file_name = "G.txt"
  with open(file_name, "r") as file:
    lines = file.readlines()

  g_info = lines[0].split()
  if len(g_info) < 3 or g_info[2] != "D":
        raise GraphHasNoDirectionException("Graph has no direction!")

  vertices_amount, edges_amount, graph_type = g_info[:3]
  
  edges_list = [line.split() for line in lines[1:]]
  vertices_list = list(set().union(*edges_list))

  for vertice in vertices_list:
    adjacency_of_vertice = []
    for edge in edges_list:
      if edge[0] == vertice:
        adjacency_of_vertice.append(edge[1])
    adjacency_list.append([vertice] + adjacency_of_vertice)

def sortList():
  global adjacency_list
  adjacency_list.sort(key=lambda x: len(x), reverse=True)
  adjacency_list_aux = []
  for child in adjacency_list:
    adjacency_list_aux.append([child[0]] + sorted(child[1:]))
  adjacency_list = adjacency_list_aux

def DFS_visit(v):
  global color, mark, d, f, adjacency_list
  index = next((i for i, lst in enumerate(adjacency_list) if lst[0] == v), None)
  color[index] = 'gray'
  mark = mark + 1
  d[index] = mark
  for vertice in adjacency_list[index][1:]:
    index_aux = next((i for i, lst in enumerate(adjacency_list) if lst[0] == vertice), None)
    if color[index_aux] == 'white':
      DFS_visit(vertice)
  color[index] = 'black'
  mark = mark + 1
  f[index] = mark

def DFS(adjacency_list):
  global color, mark, d, f
  color = ['white'] * len(adjacency_list)
  d = [0] * len(adjacency_list)
  f = [0] * len(adjacency_list)
  mark = 0
  for i,v in enumerate(adjacency_list):
    if color[i] == 'white':
      DFS_visit(v[0])

def sortResults():
  global adjacency_list, d, f
  d = [x for _, x in sorted(zip([list[0] for list in adjacency_list], d))]
  f = [x for _, x in sorted(zip([list[0] for list in adjacency_list], f))]

if __name__ == '__main__':
  try:
    readFile()
    sortList()
    DFS(adjacency_list)
    sortResults()
    print(f"qnt de vertices: {vertices_amount}")
    print(f"qnt de arestas: {edges_amount}")
    print(f"Tipo do grafo: {graph_type}")
    print(f"Lista adjacente:\n{adjacency_list}")
    print(f"Vetor d: {d}")
    print(f"Vetor f: {f}")
  except GraphHasNoDirectionException as e:
    print("Erro:", e)

