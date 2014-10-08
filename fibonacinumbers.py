
# olzhas shaikenov

def fibonacci(k):
""" This function calculates the Fiboanci sequence"""	

	fn1 = 1 		#starting fibonacci number 1=1
	fn2 = 1			#starging fibonacci number 2=1
	print fn1, fn2,
				
# Here we itereate untill the limit k 
	for i in range (2,k):	

			fn=fn1 + fn2  # main calculation for the Fib sequence
			if fn <= k:   # here we check if the fibonacci number is still less than the limit

				print fn,   # printing the fibonaci number
				fn2=fn1		# here we are reusing the vaiables fn2 and fn1
				fn1=fn
			else:
				break 




				



	
n=raw_input("Enter integer for fibonacci number limit: ")
fibonacci(int(n))
