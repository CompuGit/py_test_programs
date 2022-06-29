m = 'baccbbbdabcdbca'
n = 'abc'

everyn = [ m[i:i+len(n)] for i in range(len(m))]

res = [ everyn.index(ele) for ele in everyn if sorted(ele)==sorted(n)]

print(res)