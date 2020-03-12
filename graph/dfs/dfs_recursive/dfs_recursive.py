# Implementation de l'algorithme de Parcours en profondeur-DFS
# AUTHOR ABDOULAYE DIALLO

def dfs_recursive(graph, node, seen):
    # Pour ne pas explorer de maniere repetee les voisins 
    # d'un sommet, on marque les sommets deja visites
    # a l'aide d'un tableau de booleens
    seen[node] = True
    for neighbor in graph[node]:
        if not seen[neighbor]:
            dfs_recursive(graph, neighbor, seen)



