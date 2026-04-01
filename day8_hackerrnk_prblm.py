# Finding the scores of runner up of n participants

n = int(input())
l = map(int, input().split())
s = set(l)      #store numbers in set
l2 = list(s)    #store set elements into list

l2.sort(reverse=True) # scores in decreasing order
print(l2[1])
	