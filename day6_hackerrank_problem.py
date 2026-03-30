s = input()

isalnum_flag = False   #built string functions
isalpha_flag = False
isdigit_flag = False
islower_flag = False
isupper_flag = False

for c in s:         #is that character exist in given                               string
    if c.isalnum():
        isalnum_flag = True
    if c.isalpha():
        isalpha_flag = True
    if c.isdigit():
        isdigit_flag = True
    if c.islower():
        islower_flag = True
    if c.isupper():
        isupper_flag = True

print(isalnum_flag)
print(isalpha_flag)
print(isdigit_flag)
print(islower_flag)
print(isupper_flag)