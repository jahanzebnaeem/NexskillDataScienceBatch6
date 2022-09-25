# my_list = ['This is val1', 2, 3, ['a', 4]]
# print(my_list[3][1])
# print(len(my_list))
# print(my_list[:-1])
# my_list[0] = 'This is new val'
# print(my_list)
# print(my_list + ['new item'])
# print(my_list)
# print(my_list*2)
# my_list.append('this is new')
# print(my_list)
# my_list.pop(1)
# print(my_list)
# my_list.reverse()
# print(my_list)

# lst_1=[1,2,3]
# lst_2=[4,5,6]
# lst_3=[7,8,9]
#
# matrix = [lst_1,lst_2,lst_3]
#
# # print(matrix[1][1:])
#
# first_col = [row[0:2] for row in matrix]
#
# print(first_col)

# d = {'key1':{'nestkey':{'subnestkey':'value'}}}
# print(d['key1']['nestkey']['subnestkey'])

# t = ('one', 2, 'one', 1, 3, 'one')
# # print(t.count('one'))
# # t[0]= 'change'
# t.append('nope')
#
# l = [1,1,2,2,3,4,5,6,1,1]
#
# print(set(l))

# seq = [1,2,3,4,5]
#
# # for item in seq:
# #     print(item)
#
# for item in seq:
#     print('Yep')

# ages = {"Sam":3,"Frank":4,"Dan":29}
#
# # print(ages['Sam'])
#
# for key in ages:
#     print("This is the key")
#     print(key)
#     print("This is the value")
#     print(ages[key])
#     print("\n")

# mypairs = [(1,10),(3,30),(5,50)]
#
# for tup1,tup2 in mypairs:
#     print(tup1)
#     print(tup2)

# print(list(range(5)))

# for i in range(0,10,2):
#     print(i)

# # Starting with:
# x = [1,2,3,4]
#
# # We could do this:
# out = []
# for item in x:
#     out.append(item**2)
# print(out)

def addEvenOnly(num1,num2):
    """
    INPUT: Two numbers
    OUTPUT: False if both numbers are not even,
    the sum if both numbers ar even
    """
    if (num1 % 2!=0) or (num2 % 2 != 0):
        return False
    else:
        return num1+num2

x = addEvenOnly(1,2)
y = addEvenOnly(2,2)
print(x)
print(y)
