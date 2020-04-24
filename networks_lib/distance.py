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
    visited = np.full((num_vertices), False)
    
    # Finish this loop
    for i in range(num_vertices):
        pass
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
    available = [False for _ in range(num_vertices)]

    components = []
    
    # finish this loop
    while any(available):
        pass
    
    # this is for testing purposes remove from final solution
    components = [np.arange(num_vertices)]
    
    return components
