# Tuples
var1 = (143,"americano",6.7,False)
print(var1)

# Ordered, immutable, mix of datatype
# Adding values to a tuple
var2 = (89,82,)
var1 = var1 + var2
print(var1)
print(var2.count(82))
print(var1[2:3])

# Weather prediction
weather = (1,0,0,0,1,1,0)
sunny = 0
rainy = 0
for i in range(0,7):
    if (weather[i]==0):
        sunny+=1
    else:
        rainy+=1
if (sunny>rainy):
    print("Good weather")
else:
    print("Bad weather")