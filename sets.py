# add()     Adds an element to the set
thisset = {"olma", "anor", "gilos"}
thisset.add("uzum")
print(thisset)

thisset = {"mushuk", "kuchuk", "sigir"}
thisset.add("ot")
print(thisset)



# clear()     Removes all the elements from the set
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)

thisset = {"o'qituvchi", "dasturchi", "shifokor", 1}
thisset.clear()
print(thisset)



# copy()     Returns a copy of the set
sonlar = {"bir", "ikki", 3, 4, 5}
x = sonlar.copy()
print(x)

thisset = {"apple", "banana", "cherry"}
x = thisset.copy()
print(x)




# difference()  -  Returns a set containing the difference between two or more sets
x = {"olma", "banan", "kiwi", }
y = {"gilos", "anor", "olma"}
z = x.difference(y)
print(z)

x = {1, 5, 7, 4, 3, 2 }
y = {8, 6, 9, 4, 1}
z = x.difference(y)
print(z)




# difference_update()  -=  Removes the items in this set that are also included in another, specified set

# discard()     Remove the specified item
thisset = {"bmw", "chevrolet", "hyundai"}
thisset.discard("chevrolet")
print(thisset)

thisset = {"ali", "vali", "diyor"}
thisset.discard("vali")
print(thisset)



# intersection()  &  Returns a set, that is the intersection of two other sets
x = {"apple", "banana", "cherry"}
y = {"ananas", "kiwi", "apple"}
z = x.intersection(y)
print(z)

x = {"o'qituvchi", "dasturchi", "shifokor"}
y = {"dasturchi", "uchuvchi", "quruvchi"}
z = x.intersection(y)
print(z)



# intersection_update()  &=  Removes the items in this set that are not present in other, specified set(s)
x = {"kia", "bmw", "chevrolet"}
y = {"bmw", "hyundai"}
x.intersection_update(y)
print(x)



# isdisjoint()     Returns whether two sets have a intersection or not
x = {"apple", "banana", "cherry"}
y = {"kiwi","ananas"}
z = x.isdisjoint(y)
print(z)

x = {"apple", "banana", "cherry"}
y = {"kiwi","ananas", "apple"}
z = x.isdisjoint(y)
print(z)



# issubset()  <=  Returns True if all items of this set is present in another set
x = {"mushuk", "kuchuk"}
y = {"fil", "echki", "mushuk",  "ot", "kuchuk"}
z = x.issubset(y)
print(z)

x = {"olma", "anor"}
y = {"gilos", "anor",  "uzum", "banan"}
z = x.issubset(y)
print(z)




# issuperset()  >=  Returns True if all items of another set is present in this set
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y)
print(z)




# pop()     Removes an element from the set
fruits = {"apple", "banana", "cherry"}
fruits.pop()
print(fruits)

cars = {"bmw", "chevrolet", "kia", "hyundai"}
cars.pop()
print(cars)



# remove()     Removes the specified element
x = {"apple", "banana", "cherry"}
x.remove("cherry")
print(x)




# symmetric_difference()  ^  Returns a set with the symmetric differences of two sets
x = {"bmw", "chevrolet", "kia", "hyundai"}
y = {"kia", "ferrari", "tesla"}
x.symmetric_difference_update(y)
print(x)



# union()	|	Return a set containing the union of sets
x = {"fil", "echki", "mushuk",  "ot"}
y = {"qo'y", "kuchuk", "mushuk"}
z = x.union(y)
print(z)



