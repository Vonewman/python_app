#include <stdio.h>
#include <stdlib.h>


const int MAX_NODES = 500;  // par exemple
const int MAX_ARCS = 2*MAX_NODES * MAX_NODES;  // par exemple

int nb_nodes = 0;
int nb_arcs = 0;
int arc[MAX_NODES] = {0};
int succ[MAX_ARCS], dest[MAX_ARCS];

void clear_graph(int n) {
	nb_nodes = n;
	nb_arcs = 0;
	for (int v=0; v<nb_nodes; v++)
		arc[v] = -1;
}

void add_arc(int u, int v) {
	succ[nb_arcs] = arc[v];
	dest[nb_arcs] = v;
	arc[u] = nb_arcs++;
}

#define forall_neighbors(u, v) \
	for (int e=arc[u]; e!=-1; && (v=dest[e], 1); e=succ[e])

int main(void)
{
	return EXIT_SUCCESS;
}


