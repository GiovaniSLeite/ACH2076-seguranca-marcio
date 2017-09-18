from random import randint
SIZE = 1000
s = ""
for j in range(SIZE):
	for i in range(SIZE):
		s = "%s%s" % (s,randint(0,1))
print s