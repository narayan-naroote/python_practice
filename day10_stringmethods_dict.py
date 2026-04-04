#dictionary = { "key" : "value" }
Birthday = {
"chandan" : "14-2-2002",
"narayan" : "7-11-2007",
"darshan" : "4-7-2005"
}
print(Birthday.items())#Creates list of tupples
print(Birthday)

Birthday.pop("chandan")#pop = remove element
print(Birthday)

del Birthday["narayan"] #another way to remove element
print(Birthday)
