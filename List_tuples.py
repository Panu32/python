#List is a Container to store set of Values Of any datatype

#STRINGS ARE IMMUTABLE
#LISTS ARE MUTABLE
l= [1,"Hi","Hello",89,False]
print(l[1:4]) #index 4 not included upto 3 only

#METHODS
l.append("GoodBye")
print(l)

#l.reverse()
print(l)

l.insert(1,"beforeHi")
print(l)
l.pop()
print(l)
#l.sort

#TUPLES
#TUPLES ARE IMMUTABLE
tup= (1,2,3,4,5,"ROHAN","JOHN")

print(tup.count(4))
print(4 in tup)


