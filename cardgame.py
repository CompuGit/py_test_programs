cards = '10011101001'
res = list(cards)
#1 - filp all
#0 - remove

while len(res)>1:
	if res[0] == '1':
		for i in range(1,len(res)):
			if res[i]=='0':
				res[i]='1'
			elif res[i]=='1':
				res[i]='0'
		res.pop(0)

	elif res[0]=='0':
		res.pop(0)
	else:
		print('error found.!')
		break

if res[0] == '1':
	print('win')
else:
	print('loose')


