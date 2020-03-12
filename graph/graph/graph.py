graph = {'A' : ['B', 'F'],
         'B' : ['A', 'C'],
         'C' : ['B', 'D'],
         'D' : ['C', 'E'],
         'E' : ['D', 'F'],
         'F' : ['E', 'A']}

def find_path(graph, start, end, path=[]):
    " Parcourir le graphe "
    path = path + [start]


    if start == end:
        print("Arrivee")
        return path

    for node in graph[start]:
        print("Examen du sommet ", node)

        if node not in path:
            print("Chemin parcouru ", path)

            new_path = find_path(graph, node, end, path)
            if new_path:
                return new_path

print(find_path(graph, 'B', 'E'))
