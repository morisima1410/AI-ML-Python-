# my_set={"Apple","banana","mango","Apple","banana"}
# print(type(my_set))
# print(my_set)

# set_1={10,20,30,50,20,30,40}
# set_2={20,30,1,2,3,5,20,50}
# print(set_1)
# a=set_1.add(3)
# print(a)
# print(set_1)
# print(set_1.add(6))
# print(set_1)
# print("update:",set_1.update([11,22,5]))
# print(set_1)
# print("remove:",set_1.remove(40))
# print(set_1)

# print("discard:",set_2.discard(2))
# print(set_2)
# print("pop",set_2.pop())
# print(set_2)
# print(set_1)
# print(set_2)
# a=set_1.union(set_2)
# print("union:",set_1)#coman value
# print(set_1)
# print(set_2)
# a=set_1.difference(set_2)#difference
# print("diff:",a)

# a=set_1.intersection(set_2)
# print(a)



a={1,2,3,4,5,1,2,3}
b={10,20,30,40}
print(a.update([6,7]))
print(a)
print(a.remove(2))
print(a)
print(b.pop())
print(b)
print(a.discard(4))
print(a)