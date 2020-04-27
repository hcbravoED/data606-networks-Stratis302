import numpy as np
from collections import deque

## TODO: Implement this function
##
## Implements the breadth-first algorithm of Girvan-Newman to compute
##   number (fractional) of shortest paths starting from a given vertex
##   that go through each edge of the graph
##
## Input:
##   - vertex (int): index of vertex paths start from
##   - mat (np.array): n-by-n adjacency matrix
##
## Output:
##   (np.array): n-by-n edge count matrix
##
## Note: assume input adjacency matrix is binary and symmetric
def edge_counts(vertex, mat):
    num_vertices = mat.shape[0]
    res = np.zeros((num_vertices, num_vertices))
    shortest_path_dist = np.zeros(num_vertices)
    shortest_path_number = np.zeros(num_vertices)
    visited = np.full((num_vertices), False)
    Q = deque()
    Q.append([vertex, 0])
    
    while len(Q) > 0:        #This while loop finds shortest paths, and their lengths
        x = Q.popleft()
        #print(x)
        visited[x[0]] = True
        #print(x[0])
        #print(visited)
        shortest_path_dist[x[0]] = x[1]
        print(shortest_path_dist)
            
        neighbors = np.where(mat[x[0],:]>0)[0]    
        #print(neighbors)
        for w in neighbors:
            if visited[w] == False:
                Q.append([w, x[1] + 1])
                visited[w] = True
        #print(Q)
           
    for i in range(shortest_path_dist) #This for loop finds the number of shortest paths from the original vertex to any other
        u = np.argmin(shortest_path_dist)
        shortest_path_number[u] += 1
        neighbors = np.where(mat[u,:]>0)[0]
        for w in neighbors:
            shortest_path_number[w] += 1

    

    
    for i in range(num_vertices):  #This nested loop confirms that the separate nodes are left out of the equation
        for j in range(num_vertices):
            if i == j:
                res[i, j] = 0
    
    
    
    return res

## Compute edge betweeness for a graph
## 
## Input: 
##   - mat (np.array): n-by-n adjacency matrix. 
##
## Output:
##   (np.array): n-by-n matrix of edge betweenness
##
## Notes: Input matrix is assumed binary and symmetric
def edge_betweenness(mat):
    res = np.zeros(mat.shape)
    num_vertices = mat.shape[0]
    for i in range(num_vertices):
        res += edge_counts(i, mat)
    return res / 2.