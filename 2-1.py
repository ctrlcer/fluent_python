#2-1
symbols = "$%^&*"
codes = []
for symbol in symbols:
	codes.append(ord(symbol))

print(codes)


#2-2

symbols = "$%^&*"
codes = [ord(symbol) for symbol in symbols]
print(codes)

x = 'my precious'
dummy = [ord(x) for x in x]
print(x)
print(dummy)
