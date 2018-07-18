Graph = {'A': ['B', 'E', 'G'],
         'B': ['C'],
         'C': ['D', 'E'],
         'D': ['F'],
         'E': ['C', 'F', 'G'],
         'F': [],
         'G': ['A']}


def test(searcher):
    print(searcher('E', 'D', Graph))
    for x in ['AF', 'BF', 'DA']:
        print(x, searcher(x[0], x[1], Graph))


#############################
# Recursive
#############################

def search_1(start, goal, graph):
    solns = []
    generate_1([start], goal, solns, graph)
    solns.sort(key=lambda x: len(x))
    return solns


def generate_1(path, goal, solns, graph):
    state = path[-1]
    if state == goal:
        solns.append(path)
    else:
        for arc in graph[state]:
            if arc not in path:
                generate_1(path + [arc], goal, solns, graph)


#############################
# Path stack
#############################

def search_2(start, goal, graph):
    solns = generate_2(([start], []), goal, graph)
    solns.sort(key=lambda x: len(x))
    return solns


def generate_2(paths, goal, graph):
    solns = []
    while paths:
        front, paths = paths
        print('Front:', front)
        state = front[-1]
        if state == goal:
            solns.append(front)
        else:
            for arc in graph[state]:
                if arc not in front:
                    print('1:', paths)
                    paths = (front + [arc]), paths
                    print('2:', paths)
    return solns


if __name__ == '__main__':
    test(search_2)
