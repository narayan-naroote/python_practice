l = [
    {"name": "narayan", "marks": 89},
    {"name": "amar", "marks": 66},
    {"name": "rahul", "marks": 65}
]

marks_list = [i["marks"] for i in l]

uniq_marks = sorted(set(marks_list))

second_lowest_marks = uniq_marks[1]

names = []
for i in l:
    if i["marks"] == second_lowest_marks:
        names.append(i["name"])

names.sort()

for name in names:
    print(name)


#0utput
amar