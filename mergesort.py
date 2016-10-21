def merge_sort(lst):
	if len(lst) <= 1:
		return lst
	left = merge_sort(lst[:int(len(lst)/2)])
	right = merge_sort(lst[int(len(lst)/2) : int(len(lst))])
	result = []

	while len(left)>0 and len(right)>0:
		if left[0] > right [0]:
			result.append(right.pop(0))
		else:
			result.append(left.pop(0))

	if len(left)>0:
		result.extend(merge_sort(left))
	else:
		result.extend(merge_sort(right))
	return result

def main():
	L = [2,4,6,1,2,55,77,436,797,65]
	print(merge_sort(L))

if __name__ == '__main__':
	main()