records = [ ]
s = set()

for _ in range(int(input())):#Takes number of students
	name = input("name:")
	score  = float(input("score:"))
	records.append([name,score])#add the name and marks into records list
	s.add(score)# removes dublicate marks
sec_low_score = sorted(s)[1]
sec_low_name = [ ]
	
for name,score in records:
	if score == sec_low_score:
		sec_low_name.append(name)
for name in sorted(sec_low_name):
			print(name)