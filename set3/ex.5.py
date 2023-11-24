class Bug :
	counter = 0
	
	def __init__ (self) :
		Bug.counter += 1
		self.id = Bug.counter
		
	def __del__ (self) :
		Bug.counter -= 1
		print ("End of ID = " + str(self.id) + ", L = " + str(Bug.counter))
	
	def __str__ (self) :
		return "Bug ID = " + str(self.id) + ", L = " + str(Bug.counter)

bugs = []
for i in range(100) :
    bugs.append (Bug ())
    print (bugs[-1])