##PP11 - Prime Number Checker
num = int(input('Insert a number'))
a = [i for i in range(2, num) if num %i == 0]

def is_prime(n):
	if num > 1:
		if len(a) == 0:
			print('prime')
		else:
			print('NOT prime')
	else:
		print('NOT prime')
	
is_prime(num)
