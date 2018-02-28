import random

def floatc():
	u = random.uniform(-20.0,20.0)
	return round(u,3)

def createarray(n):
	x, y, xcp = [floatc() for j in range(n)], [], 0
	for i in range(len(x)):
		a = x[i]/len(x); xcp+=a;
	for i in range(len(x)):
		b = round(x[i]/xcp,3); y.append(b)
	print(x); print(y)

if __name__ == "__main__":
	for i in range(5, 25, 5):
		createarray(i)
