#tuple
print("Accessing elements in tuple\n")
ele1 = ('python', 'anaconda', 'java', 1991,1999,2001)
ele2 = (1,2,3,4,8)
print(ele1)
print(ele2)
#Accessing the tuple values
tuple1 = ele1[0]
tuple2 = ele2[2:4]
print("ele1[0]:", tuple1)
print("ele2[2:4]:", tuple2)



print("\n\nlenght of tuple\n")
tup = (1000,2000, 1997, 2000);
List=[100,200,300,400,500];
print (tup);
print ("Length of Tuple=",len(tup));
print("Maximum value=",max(tup));
print("Minimum value=",min(tup));
print(tuple(List))




# Write python program to convert String into tuples?
print("\n\nconvert string to tuple\n")
s="python"
print(tuple(s))


#get the 4th element from first and 4th element from last of a tuple ?
print("\n\nfirst and 4th element from last of a tuple\n")

tuplex = ("w", "e", "l", "c", "o", "m", "e", "s", "q", "l")
print(tuplex)
item = tuplex[3]
print(item)
item1 = tuplex[-4]
print(item1)



#get the element except first and last of tuple?
print("\n\nexcept first and last of tuple\n")
tuplex = ("w", "e", "l", "c", "o", "m", "e", "s", "q", "l")
print(tuplex)
print(tuplex[1:-1])



