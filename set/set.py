my_set={"Apple","banana","mango","Apple","banana"}
print(type(my_set))
print(my_set)

set_1={10,20,30,50,20,30,40}
set_2={20,30,1,2,3,5,20,50}
print(set_1)
a=set_1.add(3)
print(a)
print(set_1)
print(set_1.add(4))
print(set_1.update([1,2,5]))
print(set_1.remove(20))
print(set_1.discard(2))
print(set_1.pop())
print(set_1)
print(set_2)
a=set_1.union(set_2)
# # print(set_1)
# print(set_1)
# print(set_2)
a=set_1.difference(set_2)
a=set_1.intersection(set_2)
print(a)


