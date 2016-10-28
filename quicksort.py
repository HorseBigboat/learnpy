
#Error when adding more int into the list to be sorted
#RecursionError: maximum recursion depth exceeded in comparison
import random

def quicksort(lst,low,high):
	i = low; j = high; key = lst[i]
	if i >= j:
		return lst
	else:
		while(i<j):
			while i<j and lst[j] >= key:
				j -= 1
			temp = lst[i]
			lst[i] = lst[j]
			lst[j] = temp
			i += 1
			while i<j and lst[i] <= key:
				i += 1
			temp = lst[i]
			lst[i] = lst[j]
			lst[j] = temp
			j -= 1
		quicksort(lst,low,i-1)
		quicksort(lst,j+1,high)
		return lst
	
def main():
	L = []
	for n in range(0,9):
		L.append(random.randint(0,1000))
	print(L)
	print(quicksort(L,0,len(L)-1))

if __name__ == '__main__':
	main()
