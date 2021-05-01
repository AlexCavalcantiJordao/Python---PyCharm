def Fatorial(num = 1) :
	f = 1
	for c in range(num,0, -1) :
		f *= c
		return f


f1 = Fatorial(5)
f2 = Fatorial(4)
f3 = Fatorial()
print(f" O resultado são {f1}, {f2} e {f3} ")