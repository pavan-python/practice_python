#Accessing Values in Lists
print("\n\ncreating list\n")
mylist1 = ['python', 'java', 1991, 2001];
mylist2 = [1, 2, 3, 4, 5, 6, 7 ];
print(mylist1)
print(mylist2)
print("\n\nAccessing Values\n")
print ("list1[0]: ", mylist1[0])
print ("list2[1:5]: ", mylist2[1:5])


#Updating Lists
print("\n\nUpdating Lists\n")
list = ['python', 'java', 1991, 2001];
print ("Value available at index 2 : ")
print (list[2])
list[2] = 2003;
print ("New value available at index 2 : ")
print (list[2])


#Delete List Elements
print("\n\nDelete List Elements\n")
list1 = ['python', 'java', 1991, 2001];
print (list1)
del list1[2];
print ("After deleting value at index 2 : ")
print (list1)


#length of the list
print("\n\nlength of list\n")
list1, list2 = [123, 'abc', 'zara'], [456, 'xyz']

print ("First list length : ", len(list1))
print ("Second list length : ", len(list2));


# max values in the list
print("\n\nmax value in list\n")
list1, list2 = ['xya', 'xyz', 'zara', 'abc'], [456, 700, 200]
print(list1)
print(list2)
print ("Max value element : ", max(list1))
print ("Max value element : ", max(list2))


#min values in the list
print("\n\nmin value in list\n")
list1, list2 = ['xya', 'xyz', 'zara', 'abc'], [456, 700, 200]
print(list1)
print(list2)
print ("Min value element : ", min(list1))
print ("Min value element : ", min(list2))


#append list
print("\n\nappend list(ending)\n")
myList = [123, 'xyz', 'zara', 'abc'];
print(myList)
myList.append( 2001 );
print (" After Updated List : ", myList);


#insert method
print("\n\ninsert elements in list\n")
myList = [123, 'xyz', 'zara', 'abc'];
print(myList)
myList.insert(1,1991)
print ("After Insert elemnts in List : ", myList);


#remove method 
print("\n\nRemove elements in list\n")
myList = [123, 'xyz', 'zara', 'abc'];
print(myList)
myList.remove(123)
print("After remove elements list:", myList)

#reverse list
print("\n\nrevere the list\n")
myList = [123, 'xyz', 'zara', 'abc', 'rama'];
myList.reverse();
print ("After reverse List : ", myList);


#remove duplicate elements in list
print("\n\nremove duplicate values\n")
a=[10,20,30,20,50,60,10,10,20,40,30,20,50,60]
print("Before remove dupplicates :",a)
new = []
for x in a:
    if x not in new:
        new.append(x)
print("After remove duplicates:", new)



#copy the original lements into new one
print("\n\nclone or copy the list\n")
originallist = ['python', 'java', 'c', 'c++','mule']
print(originallist)
mylist1 = originallist.copy()
print(mylist1)
mylist2=list(originallist)    #list() or copy() both functions are same copy the original list
print(mylist2)



#specified list after removing the 0th, 4th and 5th elements. 
print("\n\n")
# except 0 ,4,5
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(color[1],color[2],color[3])
print(color[1:4])










