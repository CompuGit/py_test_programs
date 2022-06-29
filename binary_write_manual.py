''''
with open('./bin_nums.txt','bw') as bin_file:
    for i in range(16):
        bin_file.write(bytes([i]))
'''

with open('./bin_nums','bw') as bin_file:
    bin_file.write(bytes(range(16)))

with open('./bin_nums','rb') as bin_file:
    for b in bin_file:
        print(b)


a = 65534   #FF FE
b = 65535   #FF FF
c = 2998302 #00 2D C0 1E

with open('./bin2','wb') as bin_file:
    bin_file.write(a.to_bytes(2, 'big'))
    bin_file.write(b.to_bytes(2, 'big'))
    bin_file.write(c.to_bytes(4, 'big'))
    bin_file.write(c.to_bytes(4, 'little'))

with open('./bin2','rb') as bin_file:
    d = int.from_bytes(bin_file.read(2), 'big')
    print(d)
    e = int.from_bytes(bin_file.read(2), 'big')
    print(e)
    f = int.from_bytes(bin_file.read(4), 'big')
    print(f)
    g = int.from_bytes(bin_file.read(4), 'big')
    print(g)