import time

results, app = [["Точность","Число PI","Время выполнения","7 Знаков постоянны"]], []

def timer(f):
	def tmp(*args, **kwargs):
		t = time.time()
		res = f(*args, **kwargs)
		app.append(str(round((time.time()-t),2))+' с.'); app.append("Нет")
		results.append(app)
		return res

	return tmp

def f(n):
	return ((-1)**(n+1))/(2*n-1)

@timer
def pi(eps):
	n,s,s1,s2 = 1,0,0,0
	while (True):
		s1 = f(n); s2 = f(n+1); s+=f(n)
		n+=1
		if abs(s2-s1) <= eps:
			break
	app.append(4*s)

if __name__ == "__main__":
	total = 0
	for i in range(-5,-9,-1):
		app = []
		app.append('10^'+str(i))
		pi(10**i)
	for i in range(len(results)):
		if (i > 1):
			a = str(results[i][1])
			b = str(results[i-1][1])
			a = a[0:9]; b = b[0:9]
			if (a == b):
				results[i][3] = "Да"
	print('Программа завершена. Результат:')
	for i in range(len(results)):
		if i > 0:
			c = results[i][2]; c = c[0:len(c)-3]
			total+=float(c)
		for j in range(len(results[i])):
			print(results[i][j], end=' ')
		print()
	total = round(total,2)
	print(total)


