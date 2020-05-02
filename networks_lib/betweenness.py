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
    level = np.zeros(num_vertices)
    shortest_path_number = np.zeros(num_vertices)
    node_credits = np.zeros(num_vertices)
    edge_credits = []
    visited = np.full((num_vertices), False)
    Q = deque()
    Q.append([vertex, 0])

    while len(Q) > 0:       #Step 1 of Girvan-Newman Algorithm, finds levels of all nodes, which are the lengths of the shortest paths from
        x = Q.popleft()     #the original vertex to the node
        visited[x[0]] = True
        shortest_path_dist[x[0]] = x[1]
        level[x[0]] = x[1]

        neighbors = np.where(mat[x[0],:]>0)[0]
        for w in neighbors:
            if visited[w] == False:
                Q.append([w, x[1] + 1])
                visited[w] = True
    counter = [] #This counts which nodes have already been checked

                                                 #Step 2 of Girvan-Newman Algorithm
    for i in range(num_vertices):                #This for loop finds number of shortest paths that reach each node from the root
        u = np.argmin(shortest_path_dist) 
        counter.append(u)                 #Counter checks which nodes have already been visited
        for j in range(num_vertices): #This for loop and nested if statements find the number of shortest paths to each node from the root.
            if shortest_path_dist[j] == shortest_path_dist[u] + 1:
                if j not in counter:
                    if mat[u, j] == 1:
                        shortest_path_number[j] += 1
        shortest_path_dist[u] = np.inf

    shortest_path_number[vertex] = 1

    counter.clear()
    for i in range(num_vertices): #Step 3: using shortest_path_number and level find credit for each edge and node
        parents = []
        a = np.argmax(level)      
        counter.append(a)
        node_credits[a] += 1
        for j in range(num_vertices): #This for loop and if statement find parents and edge connections
            if (level[j] == level[a] - 1) & (mat[a, j] == 1) & (j not in counter):
                    parents.append(j)
        for k in parents:                              #This for loop finds the credit for edge connections and for nodes, 
            res[a,k] = node_credits[a]/len(parents)    #and places credit for edge connections in the result matrix
            res[k,a] = node_credits[a]/len(parents)
            node_credits[k] += node_credits[a]/len(parents)


        level[a] = -1
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
