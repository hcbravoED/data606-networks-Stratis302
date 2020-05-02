import numpy as np
from random import randint
from random import seed

## TODO: Implement this function
##
## Input:
##  - dmat (np.array): symmetric array of distances
##  - K (int): Number of clusters
##
## Output:
##   (np.array): initialize by choosing random number of points as medioids
def random_init(dmat, K):
    num_vertices = dmat.shape[0]
    medioids = np.arange(K)
    seed()
    hold_seeds = []
    for i in range(K):
        interm = randint(0, num_vertices - 1)
        while interm in hold_seeds:             #Checking that the vertex is different from others
            interm = randint(0, num_vertices)
        hold_seeds.append(interm)
    medioids = np.array(hold_seeds)    
                
    return medioids

## TODO: Implement this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - medioids (np.array): indices of current medioids
##
## Output:
##   - (np.array): assignment of each point to nearest medioid
def assign(dmat, medioids):
    num_vertices = dmat.shape[0]
    compare_m = dmat[medioids,:]
    indices = np.argmin(compare_m, 0)
    return indices

## TODO: Implement this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - assignment (np.array): cluster assignment for each point
##   - K (int): number of clusters
##
## Output:
##   (np.array): indices of selected medioids
def get_medioids(dmat, assignment, K):
    medioids = np.zeros((K), dtype = np.int)
    
    for i in range(K):
        index = np.where(assignment == i)
        index = np.array(index)
        medioid_m = dmat[index, index.transpose()]
        sums = medioid_m.sum(axis = 0)
        ind_in_small = np.argmin(sums)
        medioids[i] = index[0, ind_in_small]
        
    return medioids

## TODO: Finish implementing this function
##
## Input:
##   - dmat (np.array): symmetric array of distances
##   - K (int): number of clusters
##   - niter (int): maximum number of iterations
##
## Output:
##   - (np.array): assignment of each point to cluster
def kmedioids(dmat, K, niter=10):
    num_vertices = dmat.shape[0]

    # we're checking for convergence by seeing if medioids
    # don't change so set some value to compare to
    old_medioids = np.full((K), np.inf, dtype=np.int)
    medioids = random_init(dmat, K)

    # this is here to define the variable before the loop
    assignment = np.full((num_vertices), np.inf)

    it = 0
    while np.any(old_medioids != medioids) and it < niter:
        it += 1
        old_medioids = medioids

        # finish implementing this section
        assignment = assign(dmat, medioids)
        medioids = get_medioids(dmat, assignment, K)

    return assignment
