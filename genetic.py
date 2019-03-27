import numpy as np, itertools, progressbar
from collections import Counter

def shuffle(matrix):
	np.random.shuffle(matrix)
	if wrong(matrix): shuffle(matrix)
	return matrix

def mutation(child):
    while wrong(child):
        pos, null = [], []
        for x in range(len(child)):
            if sum(child.T[x]) > 1: pos.append(x)
            if sum(child.T[x]) == 0: null.append(x)
        i = np.where(child.T[pos[0]] == 1)[0][0]
        child[i, pos[0]], child[i, null[0]]  = 0,1
    return child

def wrong(child):
	return sum([1 if (sum(child[i]) != 1 or sum(child.T[i]) != 1) else 0 for i in range(len(child))])

def random_pos(indexes = []):
    while len(indexes) != 4:
    	idx = np.random.randint(0,15)
    	if not idx in indexes: indexes.append(idx)
    return indexes

def interval(y, ost = 0):
    P = []
    for i in range(len(y)):
    	P.append(y[i]/sum(y)*100+ost); ost = P[i]
    return P

def cross(dad, mom, child = [], variant = 0):
	child = np.zeros((4, 4))
	for i in range(len(dad)):
		dad_p, mom_p = np.where(dad[i] == 1)[0][0], np.where(mom[i] == 1)[0][0]
		j = int(round((dad_p+mom_p)/2)) if variant == 0 else min(dad_p, mom_p + np.random.randint(0, abs(dad_p-mom_p)))
		child[i,j] = 1
	if wrong(child): mutation(child)
	return np.array(child)

def ability(A, population):
    y = [sum((A*item).ravel()) for item in population]
    return (y, sum(y)/len(y))

def rnd_poses(P, nums= [], k = 0):
    M = list(P)
    P.extend([np.random.randint(0,99) for i in range(4)])
    for item in sorted(P):
    	if item != M[k]: nums.append(k)
    	else: k+=1
    return nums

def evolution(y, population, var = 0):
    nums = rnd_poses(interval(y[0]))
    best = list(itertools.product([pop[idx] for idx in nums],[pop[idx] for idx in nums]))
    newpop = [best[idx] for idx in random_pos()]
    return [cross(*item, variant = var) for item in newpop]

if __name__ == "__main__":
    A = np.array([[100, 150, 90, 200],
         [200, 100, 70, 150],
         [250, 80,  70, 100],
         [190, 100, 120, 200]])
    results = []
    bar = progressbar.ProgressBar().start()
    for i in range(100):
      bar.update(i)
      pop = [shuffle(np.identity(4)) for i in range(4)]
      Y, Y_prev = ability(A, pop), 0
      while(True):
        pop = evolution(Y, pop, 0)
        Y = ability(A, pop)
        if abs(Y[1] - Y_prev) <= 0: break
        Y_prev = Y[1]
      results.append(max(Y[0]))
    bar.finish()
    c = Counter(results)
    print('Решение', max(c, key=c.get))
