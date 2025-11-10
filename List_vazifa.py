# append()  Adds an element at the end of the list
fanlar = ["matematika", "informatika", "fizika"]
fanlar.append("biologiya")
print(fanlar)

hayvonlar = ["mushuk", "it", "quyon"]
hayvonlar.append("ot")
print(hayvonlar)


# clear()  Removes all the elements from the list
kasblar = ["o‘qituvchi", "shifokor", "haydovchi", "dasturchi"]
kasblar.clear()
print(kasblar)

mashinalar = ["Cobalt", "Nexia", "Malibu"]
mashinalar.clear()
print(mashinalar)


# copy()  Returns a copy of the list
# mevalar = ["apple", "banana", "cherry"]
# a = mevalar.copy()
# print(a
#
# sonlar = ["bir", "2", "uch"]
# a = sonlar.copy()
# print(a)


# count()  Returns the number of elements with the specified value
sonlar = [1,2,3,4,5,2,1]
x = sonlar.count(1)
print(x)

mashinalar = ["Cobalt", "Nexia", "Damas", "Nexia"]
x = mashinalar.count("Nexia")
print(x)


# extend()  Add the elements of a list (or any iterable), to the end of the current list
kasblar = ['shifokor', 'haydovchi', 'dasturchi']
mashinalar = ['Ford', 'BMW', 'Volvo']
kasblar.extend(mashinalar)
print(kasblar)

mevalar = ['banan', 'olma', 'shaftoli']
sonlar = [1,2,3,4,5]
mevalar.extend(sonlar)
print(mevalar)



# index()  Returns the index of the first element with the specified value
sonlar = [1,5,2,7,3,4,6]
x = sonlar.index(3)
print(x)

mevalar = ['apple', 'banana', 'cherry']
x = mevalar.index("cherry")
print(x)


# insert()  Adds an element at the specified position
mevalar = ['olma', 'banan', 'olcha']
mevalar.insert(2, "sariq")
print(mevalar)

ranglar = ['sariq', 'qizil', 'yashil']
ranglar.insert(1, "oq")
print(ranglar)


# pop()  Removes the element at the specified position
sonlar = [1,2,3,4,5,6]
sonlar.pop(1)
print(sonlar)

ranglar = ['sariq', 'qizil', 'yashil']
ranglar.pop(2)
print(ranglar)


# remove()  Removes the item with the specified value
mevalar = ['apple', 'banana', 'cherry']
mevalar.remove("banana")
print(mevalar)

kasblar = ["o‘qituvchi", "shifokor", "haydovchi", "dasturchi"]
kasblar.remove("shifokor")
print(kasblar)


# reverse()  Reverses the order of the list
son = [1,2,3,6,8,9]
son.reverse()
print(son)

mashinalar = ["Cobalt", "Nexia", "Damas", "Nexia"]
mashinalar.reverse()
print(mashinalar)


# sort()  Sorts the list
ranglar = ['sariq', 'qizil', 'yashil', 'oq', 'qora']
ranglar.sort()
print(ranglar)

sonlar = [5,7,3,4,2,8,9,2]
sonlar.sort()
print(sonlar)