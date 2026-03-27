1)
#passing n number of values for adding
def add(*numbers): #star or asterik
	return sum(numbers)
print(add(1,100,1))


2)

def  total_sum(*numbers):
	result = 0
	for num in numbers:
		result+=num
	return result
print(total_sum(24,5,8))

