import pprint

pp = pprint.PrettyPrinter(indent=4)


def getCycles(graph):
    """Returns an array of digraphs containing cycles. Each digraph is represented as a dictionary mapping
    vertices to its neighbouring vertices.

    """

    def getCycle(graph):
        """Return the offending cycle and last vertex visitsed if the directed
        graph has a cycle. The graph must be represented as a dictionary mapping
        vertices to iterables of neighbouring vertices. For example:

        >>> cyclic({1: (2,), 2: (3,), 3: (1,)})
        ([1, 2, 3], 1)
        >>> cyclic({1: (2,), 2: (3,), 3: (4,)})
        False

        Adapted from https://codereview.stackexchange.com/questions/86021/check-if-a-directed-graph-contains-a-cycle

        """
        visited = set()
        path = []
        path_set = set(path)
        stack = [iter(graph)]
        while stack:
            for v in stack[-1]:
                if v in path_set:
                    return path, v
                elif v not in visited:
                    visited.add(v)
                    path.append(v)
                    path_set.add(v)
                    stack.append(iter(graph.get(v, ())))
                    break
            else:
                if path:
                    path_set.remove(path.pop())
                stack.pop()
        return False

    cycles = []

    cycleTup = getCycle(graph)

    while cycleTup:
        cycle, vertex = cycleTup
        subgraph = graph.copy()

        for key in subgraph.keys():
            if key not in cycle:
                del subgraph[key]

        for key in subgraph.keys():
            if key in cycle:
                subgraph[key] = [v for v in subgraph[key] if v in cycle]

        cycles.append(subgraph)

        graph[cycle[-1]] = [x for x in graph[cycle[-1]] if x is not vertex]

        cycleTup = getCycle(graph)

    return cycles


if __name__ == "__main__":
    graph = {
        1: (2,),
        2: (3, 4),
        3: (1,),
        4: (8,),
        5: (3,),
        6: (1,),
        7: (6,),
        8: (7,)
    }

    cycles = getCycles(graph)

    pp.pprint(cycles)
