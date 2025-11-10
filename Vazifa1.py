# # capitalize()  Converts the first character to upper case
# a = "salom mening ismim laylo."
# x = a.capitalize()
# print (x)

# b = "salom dunyo."
# c = b.capitalize()
# print (c)

# # casefold()  Converts string into lower case
# d = "SALOM DUNYO!"
# x = d.casefold()
# print(x)

# matn = "Mening ISmim Laylo!"
# x = matn.casefold()
# print(x)

# # center()  Returns a centered string
# matn = "meva"
# x = matn.center(30)
# print(x)

# matn = "olma sharbati"
# x = matn.center(25)
# print(x)

# # count()  Returns the number of times a specified value occurs in a string
# matn = "1859635285645"
# x = matn.count("5")
# print(x)

# matn = "menga olma va olma sharbati juda yoqadi"
# x = matn.count("olma")
# print(x)

# # encode()  Returns an encoded version of the string
# c = "Tojiboyeva Laylo"
# a = c.encode()
# print(a)

# # endswith()  Returns true if the string ends with the specified value
# matn = "Bu men Laylo."
# a = matn.endswith("!")
# print(a)

# matn = "bugun havo juda sovuq."
# a = matn.endswith(".")
# print(a)

# # expandtabs()  Sets the tab size of the string
# matn = "T\to\tj\ti\tb\to\ty\te\tv\ta\t"
# x =  matn.expandtabs(2)
# print(x)

# # find()  Searches the string for a specified value and returns the position of where it was found
# matn = "Salom, mening ismim Laylo."
# x = matn.find("Laylo")
# print(x)

# matn = "Salom, mening ismim Laylo."
# x = matn.find(",")
# print(x)

# # format()  Formats specified values in a string
# matn = "Bu mahsulot {narx:.1f} so'm turadi!"
# print(matn.format(narx = 14.67))

# matn = "{ism}ning o'rtacha bahosi {baho:.1f}bal!"
# print(matn.format(ism="Laylo",baho = 4.333))


# # format_map()  Formats specified values in a string
# # index()  Searches the string for a specified value and returns the position of where it was found
# matn = "Salom dunyo."
# x = matn.index("dunyo")
# print(x)

# # isalnum()  Returns True if all characters in the string are alphanumeric
# matn = "Salom1dunyo2"
# x = matn.isalnum()
# print(x)

# matn = "Salom dunyo"
# x = matn.isalnum()
# print(x)

# # isalpha()  Returns True if all characters in the string are in the alphabet
# matn = "TojiboyevaL"
# x = matn.isalpha()
# print(x)

# matn = "Tojiboyeva_Laylo"
# x = matn.isalpha()
# print(x)

# # isascii()  Returns True if all characters in the string are ascii characters
# txt = "Salom123"
# x = txt.isascii()
# print(x)

# matn = "3-sinf o'quvchisi Ali"
# x = matn.isascii()
# print(x)

# # isdecimal()  Returns True if all characters in the string are decimals
# matn = "salom123"
# x = matn.isdecimal()
# print(x)

# sonlar = "23483"
# x = sonlar.isdecimal()
# print(x)

# # isdigit()  Returns True if all characters in the string are digits
# son = "50800"
# x = son.isdigit()
# print(x)

# # isidentifier()  Returns True if the string is an identifier
# matn = "_laylo"
# x = matn.isidentifier()
# print(x)

# matn = "1laylo"
# x = matn.isidentifier()
# print(x)

# # islower()  Returns True if all characters in the string are lower case
# matn = "men laylo tojiboyeva!"
# x = matn.islower()
# print(x)

# # isnumeric()  Returns True if all characters in the string are numeric
# son = "565543"
# x = son.isnumeric()
# print(x)

# # isprintable()  Returns True if all characters in the string are printable
# matn = "Assalomu aleykum #1?"
# x = matn.isprintable()
# print(x)

# # isspace()  Returns True if all characters in the string are whitespaces
# matn = "   "
# x = matn.isspace()
# print(x)

# # istitle()  Returns True if the string follows the rules of a title
# matn = "Bugun Havo Sovuq"
# a = matn.istitle()
# print(a)

# matn = "Salom dunyo"
# a = matn.istitle()
# print(a)

# # isupper()  Returns True if all characters in the string are upper case
# matn = "TOJIBOYEVA LAYLO"
# x = matn.isupper()
# print(x)


# # join()  Joins the elements of an iterable to the end of the string
# a = ("Olma", "Anor", "Uzum")
# b = "#".join(a)
# print(b)

# # ljust()  Returns a left justified version of the string
# matn = "kuz"
# x = matn.ljust(10)
# print(x, "mening sevimli faslim.")


# # lower()  Converts a string into lower case
# matn = "TOJIBOYEVA laylo"
# x = matn.lower()
# print(x)


# # lstrip()  Returns a left trim version of the string
# matn = "     kuz     "
# x = matn.lstrip()
# print("mening sevimli faslim", x )


# # maketrans()  Returns a translation table to be used in translations
# matn = "Salom Dunyo"
# a = str.maketrans("D", "H")
# print(matn.translate(a))


# # partition()  Returns a tuple where the string is parted into three parts
# a = "Bugun havo sovuq"
# x = a.partition("Bugun")
# print(x)

# a = "Bugun havo sovuq"
# x = a.partition("Salom")
# print(x)

# # rfind()  Searches the string for a specified value and returns the last position of where it was found
# txt = "sevimli faslim kuz, oltin kuz"
# x = txt.rfind("kuz")
# print(x)

# # rindex()  Searches the string for a specified value and returns the last position of where it was found
# matn = "salom laylo , qandaysiz laylo"
# x = matn.rindex("laylo")
# print(x)


# # rjust()  Returns a right justified version of the string
# matn = "olma"
# a = matn.rjust(20)
# print(a, "eng sevimli mevam.")


# # rpartition()  Returns a tuple where the string is parted into three parts
# txt = "quyoshli ob havo"
# x = txt.rpartition("havo")
# print(x)

# txt = "quyoshli ob havo"
# x = txt.rpartition("salom")
# print(x)


# # rsplit()  Splits the string at the specified separator, and returns a list
# matn = "apple, banana, cherry,"
# a = matn.rsplit(", ")
# print(a)

# # rstrip()  Returns a right trim version of the string
# matn = "     banana     "
# x = matn.rstrip()
# print( x)

# matn = "     Laylo     "
# x = matn.rstrip()
# print("Tojiboyeva", x, "Azamatovna")


# # split()  Splits the string at the specified separator, and returns a list
# txt = "Assalomu aleykum hammaga"
# x = txt.split()
# print(x)


# # splitlines()  Splits the string at line breaks and returns a list
# matn = "O'zbekiston Respublikasi\n Xorazm viloyati"
# x = matn.splitlines()
# print(x)


# # startswith()  Returns true if the string starts with the specified value
# matn = "Salom Dunyo."
# x = matn.startswith("Salom")
# print(x)


# # strip()  Returns a trimmed version of the string
# a = "     olma     "
# x = a.strip()
# print(x)


# # swapcase()  Swaps cases, lower case becomes upper case and vice versa
# matn = "SALOM mening ismim LAYLO"
# x = matn.swapcase()
# print(x)


# # title()  Converts the first character of each word to upper case
# matn = "mening yoshim 19 da"
# a = matn.title()
# print(a)


# # translate()  Returns a translated string
# #use a dictionary with ascii codes to replace 83 (S) with 80 (P):
# mydict = {83:  80}
# txt = "Salom dunyo!"
# print(txt.translate(mydict))


# # upper()  Converts a string into upper case
# matn = "salom dunyo"
# x = matn.upper()
# print(x)


# # zfill()  Fills the string with a specified number of 0 values at the beginning
# son = "50"
# a = son.zfill(10)
# print(a)