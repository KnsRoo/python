import numpy as np, itertools
from collections import Counter

def shuffle(matrix):
    np.random.shuffle(matrix)
    return matrix if not wrong(matrix) else shuffle(matrix)

def rand_vector(indexes):
    return indexes if len(set(indexes)) == 4 else rand_vector([np.random.randint(0,15) for i in range(4)])

def mutation(child, pos = 0, null = 0):
    while wrong(child):
        for x in range(len(child)):
            if sum(child.T[x]) > 1: pos = x
            if sum(child.T[x]) == 0: null = x
        i = np.where(child.T[pos] == 1)[0][0]
        child[i, pos], child[i, null]  = 0, 1
    return child

def wrong(child):
	return sum([1 if (sum(child[i]) != 1 or sum(child.T[i]) != 1) else 0 for i in range(len(child))])

def cross(dad, mom, child, variant = 0):
    for i in range(len(dad)):
    	dad_p, mom_p = np.where(dad[i] == 1)[0][0], np.where(mom[i] == 1)[0][0]
    	j = int(round((dad_p+mom_p)/2)) if variant == 0 else min(dad_p, mom_p + np.random.randint(0, abs(dad_p-mom_p)))
    	child[i,j] = 1
    return np.array(child) if not wrong(child) else mutation(child)

def ability(A, pop):
    y = [sum((np.multiply(A,item)).ravel()) for item in pop]
    return (y, sum(y)/len(y))

def rand_poses(P, k = 0):
    M, nums = list(P), []
    P.extend([np.random.randint(0,99) for i in range(4)])
    for item in sorted(P):
    	if item != M[k]: nums.append(k)
    	else: k+=1
    return nums

def evolution(y, pop, var = 0):
    nums = rand_poses(list(np.cumsum([x/sum(y)*100 for x in y])))
    best = list(itertools.product([pop[idx] for idx in nums], repeat = 2))
    return [cross(*item, np.zeros((4, 4)), variant = var) for item in [best[idx] for idx in rand_vector([np.random.randint(0,15) for i in range(4)])]]

if __name__ == "__main__":
    A = np.array([[100, 150, 90, 200],
         [200, 100, 70, 150],
         [250, 80,  70, 100],
         [190, 100, 120, 200]])
    results = []
    for i in range(20):
      pop = [shuffle(np.identity(4)) for i in range(4)]
      Y, Y_prev = ability(A, pop), 0
      while(True):
        pop = evolution(Y[0], pop, 0)
        Y = ability(A, pop)
        if abs(Y[1] - Y_prev) <= 0: break
        Y_prev = Y[1]
      results.append(max(Y[0]))
    c = Counter(results)
    print('Решение', max(c, key=c.get))
