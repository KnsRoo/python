import numpy as np
import itertools
import random


def shuffle(matrix):
	np.random.shuffle(matrix)
	for i in range(len(matrix)):
		if sum(matrix[i]) != 1 or sum(matrix.T[i]) != 1: shuffle(matrix)
	return matrix

def mutation(child):
	for i in range(3):
		for z in range(3):
			j = np.where(child[i] == 1)[0][0]
			child[i][j] = 0
			child[i][(j+z)%4] = 1
			if not checkshift(child):
				return child

def checkshift(child):
	for i in range(len(child)):
		if sum(child[i]) != 1 or sum(child.T[i]) != 1: return True
	return False

def random_pos(indexes = []):
    while len(indexes) != 4:
    	idx = random.randint(0,15)
    	if not idx in indexes: indexes.append(idx)
    return indexes

def interval(y, ost = 0):
    P = []
    for i in range(len(y)):
    	P.append(y[i]/sum(y)*100+ost)
    	ost = P[i]
    return P

def cross(dad, mom, child = [], variant = 0):
	child = np.zeros((4, 4))
	for i in range(len(dad)):
		dad_p, mom_p = np.where(dad[i] == 1)[0][0], np.where(mom[i] == 1)[0][0]
		j = int(round((dad_p+mom_p)/2)) if variant == 0 else min(dad_p, mom_p + random.randint(0, abs(dad_p-mom_p)))
		child[i,j] = 1
	if checkshift(child): mutation(child)
	return np.array(child)

def ability(A, population):
    y = [sum((A*item).ravel()) for item in population]
    y0 = sum(y)/len(y)
    return (y, y0)

def rnd_poses(P, nums= [], k = 0, ):
    M = list(P)
    P.extend([random.randint(0,99) for i in range(4)])
    for item in sorted(P):
    	if item != M[k]: nums.append(k)
    	else: k+=1
    return nums

def evolution(y, population, var = 0):
    P = interval(y[0])
    nums = rnd_poses(P)
    best = [pop[idx] for idx in nums]
    best = list(itertools.product(best,best))
    newpop = [best[idx] for idx in random_pos()]
    return [cross(*item, variant = var) for item in newpop]

def loginfo(y, y0):
	print('Приспособленность популяции', y0)

if __name__ == "__main__":
    A = np.array([[100, 150, 90, 200],
         [200, 100, 70, 150],
         [250, 80,  70, 100],
         [190, 100, 120, 200]])
    pop = [shuffle(np.identity(4)) for i in range(4)]
    Y, Y_prev = ability(A, pop), 0
    loginfo(*Y)
    while(True):
    	pop = evolution(Y, pop, 0)
    	Y = ability(A, pop)
    	if abs(Y[1] - Y_prev) <= 0: break
    	Y_prev = Y[1]
    loginfo(*Y)
    print('Решение', max(Y[0]))
