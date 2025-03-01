def hornors(arr, x, n):
	p = arr[0]
	for i in range(1, n):
		p = p*x + arr[i]
	return p

arr = [3,5,6]
x = 3

print(hornors(arr, x, len(arr)))