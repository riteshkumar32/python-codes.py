#   Loops
# 1 -->while loop
cnt=1
while cnt <= 5:
    print("hello Ritesh")
    cnt+=1
    

# print elements of tuple
nums=(1,2,3,4,5,6,5,5,9)

i=0
while i<len(nums):
    if(nums[i]==5):
        print("Found")
        break
    elif(nums[i]==4):
        i+=1
        continue
    else:
        print("searching")
    i+=1 
print("End of loop")



#  FOR loop
print("For LOOP")
list=[1,6,4,9,2,3,90]
for el in list:
    print(el)


veggies=["potato","tomato","spinach","cabbage"]
for i in veggies:
    print(i)
else:
    print("END")
    
    
    
print("Range---->")
    #  RANGE----> Range functions returns a sequence of numbers ,starting from 0 by default, and increases by 1(by default),and stops before a specified number
sequence=range(5)
print(sequence[0])
print(sequence[1])
print(sequence[2])
print(sequence[3])
print(sequence[4])

#  to print loops uning range
seq=range(10)

# for i in seq:
#     print(i)

# range(start is optional?,stop is necessary,step is optional?)

print(" range (start ,stop)")
for i in range(2,10):  # range(start,stop)
    print(i)
    
print("enen numbers")
for i in range(2,10,2):  # range(start,stop,step)
    print(i)

# q --> print the umltiplication table of n
n=int(input("enter the table name\n"))
for i in range(1,11):
    print(n*i)
    
    
#  pass---> pass is a null statement that does nothing.It is used as a placeholder for future code

print("pass--->")
for i in range (1,11):
    pass
print("end of loop")






#  q --> sum upto n numbers

print(" q no 1--->")
n=5
sum=0
while(n!=0):
    sum+=n
    n-=1
print(sum)


print(" q no 2, print factorial of a number")
n=5
fact=1
while n!=0:
    fact*=n
    n-=1
print("factorial of", n ,"is ",fact)