'''
a=[10,20,30,20,50,60,10,10,20,40,30,20,50,60]
print(a)
new = []
for x in a:
    if x not in new:
        new.append(x)
print("After remove duplicates:", new)



originallist = ['python', 'java', 'c', 'c++','mule']
print(originallist)
mylist1 = originallist.copy()
print(mylist1)
mylist2=list(originallist)    #list() or copy() both functions are same copy the original list
print(mylist2)

'''
#specified list after removing the 0th, 4th and 5th elements. 

# except 0 ,4,5
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
print(color[1],color[2],color[3])
print(color[1:4])
