itr = int(raw_input())
for i in xrange(0,itr):
	inp = raw_input()
	a , b , c , d = [int(s) for s in inp.split()]
	for j in xrange(1 , b):
			c= c+(c*d)
			if c>=a:
				break
	if c>=a:
		print "ALIVE AND KICKING"
	else:
		print "DEAD AND ROTTING" 
