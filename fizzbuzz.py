#FUzz buzz game
while True:
	try:

		print "Please Enter any upper limit for FizzBuzz game"
		limit=raw_input()
		print 'This is FUZZ BUZZ GAME COUNTING TO:', limit

			

		for  i in range (1,long(limit)):

			if i%3==0:	
				print (" Fizz "),
			elif i%5==0:
				print (" buzz "),
			else:
				print i,

		
	except ValueError:
		print 'Plese enter numeric value or type exit'
		
