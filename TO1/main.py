import sys

data = sys.stdin.readlines()
n = int(data[2].split('n=')[1])
adj_list = {chave: set() for chave in range(1, n+1)}

for a in data[4:]:
  aresta = a.split()
  v1 = (aresta[0])
  v2 = (aresta[1].split("\n")[0])
  adj_list[int(v1)].add(int(v2))
  adj_list[int(v2)].add(int(v1))

def visit_neighbours(v, adj_list, visited, component):
  visited[v] = True
  component.append(v)
  for i in adj_list[v]:
    if visited[i] == False:
      visit_neighbours(i, adj_list, visited, component)

def find_components(adj_list):
  visited = {i: False for i in range(1, n+1)}
  components = []
  for v in adj_list:
    if visited[v] == False:
      component = []
      visit_neighbours(v, adj_list, visited, component)
      components.append(sorted(component))
  return components

def printComponents(components):
  output = ""
  for i in components:
    output += " ".join(map(str,i)) + '\n'
  print(output, end="")

components = find_components(adj_list)
printComponents(components)
