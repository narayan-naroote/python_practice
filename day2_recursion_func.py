#Recursion function to print numbers  from 1 to n
def Numbers(n):
		if n==0:        #base case
			return
		Numbers(n-1)    #recursive call
		print(n)        #print while coming back
Numbers(10)       # function call