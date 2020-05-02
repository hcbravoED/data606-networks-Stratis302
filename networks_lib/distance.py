import numpy as np
from collections import deque

## TODO: Implement this function
##
## input:
##   mat (np.array): adjacency matrix for graph
## 
## returns:
##   (np.array): distance matrix
##
## Note: You can assume input matrix is binary, square and symmetric 
##       Your output should be square and symmetric
def bfs_distance(mat):
    num_vertices = mat.shape[0]    
    res = np.full((num_vertices, num_vertices), np.inf)
    
    # Finish this loop
    for i in range(num_vertices):                    
        visited = np.full((num_vertices), False)
        Q = deque()
        Q.append([i, 0])
        
        while len(Q) > 0:
            x = Q.popleft()
            visited[x[0]] = True
            res[i, x[0]] = x[1]
            
            neighbors = np.where(mat[x[0],:]>0)[0]    
            for w in neighbors:
                if visited[w] == False:
                    Q.append([w, x[1] + 1])
                    visited[w] = True
    return res

## TODO: Implement this function
##
## input:
##   mat (np.array): adjacency matrix for graph
## 
## returns:
##   (list of np.array): list of components
##
## Note: You can assume input matrix is binary, square and symmetric 
##       Your output should be square and symmetric
def get_components(mat):
    dist_mat = bfs_distance(mat)
    num_vertices = mat.shape[0]
    available = [True for _ in range(num_vertices)]

    components = []
    # finish this loop
    while any(available):
        x = []
        u = np.argmax(available)
        for i in range(num_vertices):
            if dist_mat[u, i] < np.inf:
                x.append(i)
            available[u] = False
        if x not in components:
            components.append(x)
        

    
    return components
