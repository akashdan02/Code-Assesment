7#
def checkforduplicates(num):
    if len(num) == len(set(num)):
        return False
    else:
        return True
num = [2,4,6,4,6,8,9,5,7,8]
result = checkforduplicates(num)
if result:
    print('Yes,it has duplicates')
else:
    print('No duplicates')