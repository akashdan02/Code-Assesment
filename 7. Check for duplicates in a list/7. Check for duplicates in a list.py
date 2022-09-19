# 7#
num = [2,4,6,4,6,8,9,5,7,8]
empty = [] 

for i in num:
    n = num.count(i)
    if n > 1:
        if i not in empty: 
            empty.append(i)
 
print(empty)