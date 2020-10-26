my_list = [2, 1, 0]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
def is_avalbie(index):
    if my_list[index - 1] != 0:
        return 1
    else:
        return 0
print(is_avalbie(1))
print(is_avalbie(2))
print(is_avalbie(3))