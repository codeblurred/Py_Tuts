print("hello ")

var1 = "how are you ? "
var2 = "are you enjoying python coding tutroials ?"
var3 = 0.5
var4 = 3
var5 = -7
var6 = "77"

print(var4+var5)

# print(var5+var6) # will throw an error, to use it appropriately
print(int(var6)+var5)


''' 
TypeError: unsupported operand type(s) for +: 'int' and 'str'
we could not add because these are of different datatypes
in order to do so , we do typecasting : 
typecasting : basically we use it to change the type of the data . for ex: 
str()   : str(var6)
float() : int(var6)
int()   : int(var6)


'''