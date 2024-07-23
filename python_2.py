str1="this is a \n string"
str2='this is a \t string'
str3='''this is a string'''
print(str1)
print(str2)
"this is  Ritesh's car."



# Concanate two strings

final_str=str1+" " +str2
print(final_str)


#  lehgth of string 
print(len(str1))
print(len(str2))
print(len(final_str)) 


# indexing starts from 0
str="abcd"
ch=str[0]
print(ch)

# str[1]=z  // we cant manipulate data of string


# Slicing ( Accessing parts of a string)

str="Apna_college"
print(str[1:3])
print(str[1:5])
print(str[0:5])
print(str[0:len(str)])
print(str[0:])
print(str[:5])
print(str[:])

# -ve indexing  only works in slicing of string only ....
#  A(-5)  p(-4)  p(-3)  l(-2)  e(-1)
print("-ve indexing slicing  in string")
str="Apple"
print(str[-5:-2])
print(str[-2])


# String functions
print("string Functiond")
str="ritesh Kumar"

print(str.endswith("mar"))
print(str.capitalize()) #capitalize the first character of string

print(str.replace("ritesh","sahil"))

print(str)
print(str.find("t")) # return the 1st index of the first occurence of teh character or word
      
# count functions returns the count of the given letter or word
str="a bb a aaa b b a ab bb cc bb"
print(str.count("a"))
print(str.count("bb"))









#  Conditional statements if,elif,else
age=19
if(age>18):
    print("can vote")
    print("Good boy")
elif(age==18):
    print("Go Ahead")
else:
    print("You are noob")

marks=96
if(marks>=90 and marks<=100):
    print("Very good Boy")
    marks=50
if(marks>=90 or marks<=100):
    print("Very bad Boy")

