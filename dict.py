#dictionary program

#Create a dictionary
print("\n\nCreating a dictionary\n")
dic = {"name":"pavan", "age":24, "class":"python"}
print(dic)



print("\n\nAccessing values dic\n")
dict = {"Name":"pavan", "Age":24, "Class":"python"}
print ("dict['Name']: ", dict['Name'])
print ("dict['Age']: ", dict['Age'])
print ("dict['Class']",dict['Class'])



#Add Elements
print("\n\nAdd Elements in dic\n")
dict = {"Name":"pavan", "Age":24, "Class":"python"}
print("Before add elemnet:", dict)
dict["mode"] = "online"
print("After add element:", dict)



#update the elements
print("\n\nUpdate element in dict")
stud = {"name": "Pavan", "id":123, "branch":"bsc"}
print("before change elements:",stud)
stud["id"] = 456
print("after update elements:",stud)



#remove or delete the elemetns in dict
print("\n\nremoveing elemetns\n")
stud = {"name": "Pavan", "id":123, "branch":"bsc"}
print("before delete dict:",stud)
del stud["id"]
print("after delete :",stud)

print("\n\n")
#clear cll
stud1 = {"name": "Pavan", "id":123, "branch":"bsc"}
print("before clear all elements:", stud1)
stud1.clear()
print("after clear :", stud1)


