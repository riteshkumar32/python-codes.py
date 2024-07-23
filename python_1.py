print( " Hello Ritesh Bhai")
print (77+72.5)
name="Ritesh"
age=25
price=25.9999
age2=age
print (age2)


print ("Age is",age)
print("name is ",name)
print ("price=",price)


#  DATATYPE
print (type(price))
print(type(age))
print(type(name))


# 2----> String Datatype implementation (can be declared under single,double,triple cores)

name1="Ritesh"
name2='Ritesh'
name3='''Ritesh'''

print(name1)
print(name2)
print(name3)

# 3----> Boolean Datatype implementation (True ka T capital me , False ka F capital me hona chahie)
hel=False
print(hel)
print(type(hel))

# 4----> None Datatype (if we do not want to store anydata in a variable)
a=None
print(a)
print(type(a))


# ########--------------------------------------

#print sum of two numbers
a=200000
b=3
sum=a+b
print(sum)


# Multi Line Comments--->  Triple codes   """"   """"
"""""
hello 
helo
yes
"""


#  Operators (* ,+, -, /, >=,  <=,  = >,  < ,+=, *=, **, **=)

a=5
b=2
print(a/b)
print (a%b)
print (a**b) # means ->a^b
print(a==b)
print(a!=b)


#  Logical operators -->not,and ,or
print(not(True))  #takes the compliment
a=2
b=2
print (a>=b and a==b)
print (a>b or a==b)

# Type comversion -->a)conversion automatic  , b)typecasting
a=2
b=2.115
sum=a+b   # automatic convert sum to float

c="hel"
d=2
# sum1=c+d
# print(sum1) # This gives error but if we typecast the a to integer then it will be evaluated correctly
# Note only typecasting is possible if the type of data is fittable intoo it, string acnnot fit in int datatype
e=float("2.50")
print(type(e))
print(e+d)





#  Taking input 
input("enter your name")
 
name=input("enter yours name bro")
 
age=input("enter your age")
 
 # Note --> input()  result for input is always a string, but if we want to typecast the input we can do that too
val=input("enter any value")
print(type(val))   #"25"   "35.999" 
 
a=int(input("enter your Bike number"))
print(a)
 
 
 
 
#  Q--> input side of a square and outpot its area
side=float(input("enter the side"))
area=side*side
print()
print("area=",area)



