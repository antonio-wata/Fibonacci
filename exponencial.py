def multiplica(m1, m2):
	nuevo = [m1[0]*m2[0] +  m1[1]*m2[2], m1[0]*m2[1] +  m1[1]*m2[3], m1[2]*m2[0] +  m1[3]*m2[2], m1[2]*m2[1] +  m1[3]*m2[3]]
	return nuevo

def exponencial(A, n):
	if(n < 2):
		return A
	if(n == 2):
		return multiplica(A,A)
	if(n % 2 == 0):
		B = exponencial(A,(n/2))
		return multiplica(B,B)
	else:
		return multiplica(exponencial(A,(n-1)), A)

def fibo(n):
	m = [1,1,1,0]
	m2 = [1,0,1,0]
	if(n == 0 or n == 1):
		return "el numero de fibonacci " + str(n) + " es: " + str(m[2]);
	m = multiplica(exponencial(m, n),m2)
	return "el numero de fibonacci " + str(n) + " es: " + str(m[2])# + "\nel numero de fibonacci " + str(n+1) + " es: " + str(m[0])


for i in range(0,10000):
	print fibo(i)