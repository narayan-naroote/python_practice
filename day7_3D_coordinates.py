x = int(input())
y = int(input())
z = int(input())
n=3
result = [ ]
for i in range(x+1):   #runs 2times
	for j in range(y+1):  #runs 4times
		for k in range(z+1): #runs 4times
					if i+j+k!=n:
						result.append([i,j,k])
print(result)