# In python Arrays are known as Lists
# we can insert multiple datatypes data in list
marks=[12,30.5,"Ritesh",'k',55,90]
print(marks)
print(type(marks))

print(marks[-1])
print(marks[3])

print(len(marks))
marks[2]="sahil"
print(marks)



# List slicing
print(marks[1:4])  #ending index is not Included

#  Lists Function
marks=[1,4,3,5,2]
marks.append(6)   #add 6 to the end of list
print(marks)

marks.sort()     # sort the list in increasing order
print(marks)

marks.sort(reverse=True)   # sort in descending order
print(marks)

marks.reverse()  # reverse the list
print(marks)

marks.insert(0,999)  # insert 999 at 0th index and shift the other elements towards right
print(marks)

marks.remove(4)  # remove the first occurence of element(=4) in the list
print(marks)

marks.pop(2)  # delete the element present at index 2
print(marks)




print(" Tuples --->")
#  TUPLES --> THEY ARE IMMUTABLE ,I.E THEY CAN STORE ELEMENTS OF SINGLE TYPE OF DATATYPE ONLY (Difference betw List and Tuples)
#  TUPLES-->  tup[0]=78 ,we csnt do manipulation in data,neither we can add or remove elements once touple is created
tup=(2,1,4,3,5)
print(tup[0])
print(tup)
print(type(tup))

tup=(1)   # Its type is integer ,since no commas are there
print(tup)
print(type(tup))

tup=(1,)  # Now its type is tuple becoz of comma
print(tup)
print(type(tup))

# slicing in tuples
tup=(1,2,3,4,5)
print(tup[1:3])

#  TUPLE METHODS
print(" Tuple methods-->")
tup=(4,5,3,1,2,5,5)

print(tup.index(5))  # returns the index of first occurence of 5
print(tup.count(5))  # returns the count of element present in the tuple

#  Question 1(List)
print(" QUEstion no 1-->")
movie1=input("enter 1st movie")
movie2=input("enter 2nd movie")
movie3=input("enter 3rd movie")

movies=[]
movies=[movie1,movie2,movie3]
print(movies)
#  or we can use append command
movies.append(movie1)
movies.append(movie2)
movies.append(movie3)
print(movies)


# q no 2
print(" q no 2-->")
#  is palindrom ,chk list

list=[1,2,3,2,1]
copy=list.copy()
copy.reverse()
if(list==copy):
    print("Yes ,palindrome hai")
else:
    print(" palindrome nhi hai")
    

#  q no 3 , count of grade A
print("q no 3-->")
tup=('A','B','A','V','A')
print(tup.count('A'))
