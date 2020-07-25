

from util import Stack

def earliest_ancestor(ancestors, starting_node):
    parent = []
    children = []
    vertices = {}
    def addVertex(vertex):
        vertices[vertex] = set()
    
    def addEdge(v1, v2):
        vertices[v1].add(v2)
    
    def get_neighbors(vert):
        return vertices[vert]
    
    def dfs(v):
        s= Stack()
        s.push(v)
        visited = set()

        while s.size() > 0: 
            current_node = s.pop()
            print('current_node', current_node)
            if current_node not in visited : 
                visited.add(current_node)

                neighbors = get_neighbors(current_node)
                for neighbor in neighbors: 
                    s.push(neighbor)
            
        return list(visited)[0]

    


    for i in range(0, len(ancestors) - 1):
        parent.append(ancestors[i][0])
        children.append(ancestors[i][1])
        addVertex(ancestors[i][0])
        addVertex(ancestors[i][1])
        addEdge(ancestors[i][0], ancestors[i][1])

    found = dfs(starting_node)
    print('found', found)
    for key, value in vertices.items(): 
        print('value', value)
        if value == found :
            print('key', key)


