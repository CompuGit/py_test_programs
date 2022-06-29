word1 = 'Hello'
word2 = 'Hell'
pattern1 = '*l'
pattern2 = 'He?ll'
pattern3 = '?*'

def stringMatch(word,pattern):
	res = []
	flag = 0
	for a in word:
		for b in pattern:
			if a==b:
				res.append(a)
				break
			elif b=='?':
				res.append(a)
				continue
			elif b=='*':
				res += list(word[pattern.index(b):])
				flag = 1
				break
		if flag==1:
			break
	return word==(''.join(res))

print(stringMatch(word1,pattern1))
print(stringMatch(word2,pattern2))
print(stringMatch(word1,pattern3))


