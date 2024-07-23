#  Dictionary--> are used to store data values in key:value pairs
#  They are unordered,mutable(changeable), & dont allo duplicate keys

info ={
    "key1"   : "value",
    "key2" : "Ritesh",
    "Name": "Sahil",
    "age":19,
    "subject":[1,2,3,4,5],
    "tup":("no","so","ok"),
    "marks": 93.99
    
}
print(info)
print(type(info))
#  There is no indexing or ordering in dictionary

# To access values of dictionary

print(info["Name"])
print(info["age"])
print(info["subject"])
# print(info["surname"])
info["Name"]="Ritesh"  # Over  write
info["surName"]="Kumar"  # create a new member


null_dict={}
null_dict["plp"]="kni"
print(null_dict)


#  Nested dictionaries can also be created
stud={
    "name":"Ritesh",
    "subjects":{
        "phy":99,
        "chem":93
    }
}
print("Nested dictionary")
print(stud)

print(stud["subjects"]["phy"])




# Dictionary Methods
print(" Dictionary methods")
print(stud.keys()) # returns all the keys

print(list(stud.keys()))  # typecast the dictionary to list also

print(len(stud))   # return total no of key value pairs

print(stud.values()) # return s all the values of dictionary

print(stud.items()) # returns all the (key,val) pairs as tuples

print(stud.get("name"))  # returns the key according to value

stud.update({"city":"Patna"})
print(stud)

stud.update({"name":"Sahil"})
print(stud)









#  SETS-->COLLECTION OF UNORDERED ELEMENTS AND ONLY UNIQUE VALUES ARE STORED & IMMUTABLE(nON-CHANGEABLE)
print("set--->")

collection={1,5,3,4,4,1,5,"hel","hel"}
print(collection)
print(type(collection))
null_set={} #empty dictionary and not a empty set
null_set=set()  # this is a null set


#  set functions or methods
print("set functions-->")
collection=set()
collection.add(1)
collection.add(2)
collection.add(3)
collection.add("coding")

print(collection)

collection.remove(2)
print(collection)

collection.add(((5,6,7)))   # we can add a list
print(collection)

collection.pop() # remove a random value
print(collection)

collection.clear()
print(collection)

set1=set()
set1.add("coll1")
set1.add("first")
set1.add(1)


set2=set()
set2.add("coll2")
set2.add("second")
set2.add(2)
set2.add(1)

print("union is")
print(set1.union(set2)) # returns the union of two sets

print("intersection is")
print(set1.intersection(set2))   # returns the intersection of two sets






