alist = []
#print(alist[0])
#print(alist[1])
#print(alist[2])
def isavaliable(index):
    if alist[index-1] != 0:
        return 1
    else:
        return 0
    return alist[index-1]
print(isavaliable(1))
print(isavaliable(2))
print(isavaliable(3))