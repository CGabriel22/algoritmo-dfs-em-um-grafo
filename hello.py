vertices_amount, edges_amount = 0, 0
graph_type = "D"
vertices_list, edges_list, adjacency_list = [], [], []

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

if __name__ == '__main__':
  try:
    readFile()
    print(adjacency_list)
    print(f"qnt de vértices: {vertices_amount}")
    print(f"qnt de arestas: {edges_amount}")
    print(f"Tipo do grafo: {graph_type}")
  except GraphHasNoDirectionException as e:
    print("Erro:", e)

