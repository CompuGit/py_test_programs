arr = [5,3,8,2,1,10]

n = len(arr)
res = []
k=11

for i in range(n):
    lst = []         
    for j in range(i, n):
        lst.append(arr[j])

        if sum(lst) == k:
            res.append(lst)
            break

for every in res:
	for ele in every:
		print(ele, end=' ')
	print()