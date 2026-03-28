1) add = lambda a,b : a+b
print(add(6,4))



2) # Using lambda func printing in sorted order

student = [
{"name" : "narayan" , "marks" : 50},
{"name" : "amit" , "marks" : 100},
{"name" : "rahul" , "marks" : 10}
]

student.sort(key = lambda x:x["marks"],reverse=True)
print(student)

