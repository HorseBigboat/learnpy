def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1)+fib(n-2)

def main():
	n = 10
	for i in range(0,n):
		print('%s '%(fib(i)),end='')
	print('\n')

if __name__ == '__main__':
	main()