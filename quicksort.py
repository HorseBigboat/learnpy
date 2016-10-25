
#Error when adding more int into the list to be sorted
#RecursionError: maximum recursion depth exceeded in comparison

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
	L = [5,1,7,2,77,232,11,23,123,11]
	print(L)
	print(quicksort(L,0,len(L)-1))

if __name__ == '__main__':
	main()
