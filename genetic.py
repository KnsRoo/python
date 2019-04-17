import numpy as np, itertools, collections as col
from random import randint as rint

def shuffle(matrix) -> 'Генерация начальной популяции': 
    np.random.shuffle(matrix)
    return matrix if not wrong(matrix) else shuffle(matrix)

def rand_vector(indexes) -> 'Выбор 4 случайных чисел':
    return indexes if len(set(indexes)) == 4 else rand_vector(list(np.random.randint(0, len(indexes), 4)))

def mutation(child, pos = 0, null = 0) -> 'Случайная перестановка гена':
    while wrong(child):
        for x in range(len(child)):
            if sum(child.T[x]) > 1: pos = x
            if sum(child.T[x]) == 0: null = x
        i = np.where(child.T[pos] == 1)[0][0]
        child[i, pos], child[i, null]  = 0, 1
    return child

def wrong(child) -> 'Проверка на правильность генов':
	return sum([1 if (sum(child[i]) != 1 or sum(child.T[i]) != 1) else 0 for i in range(len(child))])

def cross(dad, mom, child, variant = 0) -> 'Оператор кроссовера(2 варианта)':
    for i in range(len(dad)):
    	dad_p, mom_p = np.where(dad[i] == 1)[0][0], np.where(mom[i] == 1)[0][0]
    	j = int(round((dad_p+mom_p)/2)) if variant == 0 else min(dad_p, mom_p + rint(0, abs(dad_p-mom_p)))
    	child[i,j] = 1
    return np.array(child) if not wrong(child) else mutation(child)

def ability(A, pop) -> 'Функция пр-ти и ср. пр-ть':
    y = [sum((np.multiply(A,item)).ravel()) for item in pop]
    return (y, sum(y)/len(y))

def rand_poses(P: 'Интервал', k = 0) -> 'Проверка попадания в интервалы':
    M, nums = list(P), []
    P.extend(list(np.random.randint(0, 99, 4)))
    for item in sorted(P):
    	if item != M[k]: nums.append(k)
    	else: k+=1
    return nums

def evolution(y, pop, var = 0) -> 'Шаг развития популяции':
    nums = rand_poses(list(np.cumsum([x/sum(y)*100 for x in y])))
    best = list(itertools.combinations_with_replacement([pop[idx] for idx in nums], 2))
    return [cross(*item, np.zeros((4, 4)), variant = var) for item in [best[idx] for idx in rand_vector(list(np.random.randint(0, len(best), 4)))]]

if __name__ == "__main__":
    A, R = np.array([[100, 150, 90, 200], [200, 100, 70, 150], [250, 80,  70, 100], [190, 100, 120, 200]]), []
    for i in range(20):
        pop = [shuffle(np.identity(4)) for i in range(4)]
        Y, Y_prev = ability(A, pop), 0
        while(True):
            Y = ability(A, evolution(Y[0], pop, 0))
            if abs(Y[1] - Y_prev) == 0: break
            Y_prev = Y[1]
        R.append(max(Y[0]))
    print('Решение', max(col.Counter(R), key = col.Counter(R).get))
