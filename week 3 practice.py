

#print(age >=18 and age <=65) and (not age==30)



#print(18 < age <= 65)

#print(18 < age and age <= 65)

#weight = 120
#height = 150
#print(100 < weight and weight < 200)

#print(height > 131 and height < 160)

message= "hello there my name is Hamza"
#print("hello" in message)


#if age > 100:
	#print("you are very old,")
#else:
	#print("you are young")


age = input("enter your age:")
age =int(age)
print("you are an adult" if age >= 18 else "you are not an adult yet")

for n in ["john","terry" ,"frank", "henry",]:
	print( "my name is", n,)
#the above is a string and add quoted for strings and no quotes for numbers.

for n in range(2, 12, 2):
	print(n, "to the power of", n ,"=", n**2)
