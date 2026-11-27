def min_path_complete_graph(graph):
    def dfs(graph, start, end, visited, paths, current_cost = 0):
        print(start, end)
        if(visited and start == end):
            if(len(visited) == len(graph)):
                paths.append((current_cost, [start]+visited[:]))
            return paths
        neighbors = graph[start[0]]
        for n in neighbors:
            if(n[0] in visited):
                continue
            dfs(graph, n[0], end, visited+[n[0]], paths, current_cost + n[1])
        return paths
    
    valid_paths = []
    for node in graph:
        valid_paths += dfs(graph, node, node, [], [])
        
    return sorted(valid_paths)
            
graph = {
    "a":[("d",1),("b",10),("c",10)],
    "b":[("a",2),("c",10),("d",10)],
    "c":[("d",10),("a",10),("b",2)],
    "d":[("a",10),("b",5),("c",1)]
}
print(min_path_complete_graph(graph))