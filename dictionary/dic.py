#create dictionary
 
Student={"name":"Sima" ,"age":"19","course":"AI-ML"}
print(type(Student))

#Add value

Student["city"]="s.nagar"
print(Student)

#acess value using key.
print(Student["name"])
print(Student["age"])
print(Student["course"])
print(Student["city"])
print(Student)

#delete value
print("pop",Student.pop("city"))
print(Student)