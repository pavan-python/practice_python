
# Write a program to reverse the given string
print("\nreverse the given string\n")
s = input("Enter string:")   #reverse the letters not word
print(s[::-1])




# Write a program to reverse the given string
print("\n\nreverse the given string\n")
c = input("Enter the String:")
s = c.split() #string converted into list
s.reverse()
p =" ".join(s)
print(p)




# Write a program to reverse the given string

print("\n\nreverse the given string\n")
c = input("enter string:")
s = c.split() #convert string into list
s.reverse()
s.sort()
#s.reverse()
p = " ".join(s)
print(p)





# write a python program to find area of circle
print("\n\narea of circle\n")
print("method-1\n")
import math
r = int(input("Enter Radius value:"))
print("area of circle is:", math.pi*r**2)





print("\n\n\nmethod-2\n")
from math import *
r = int(input("Enter radius value is :"))
print("area of circle is :", pi*r**2)







#string predefined function

print("\n\n\nString Examples:")
p = "Welecome to python"
p1 = "WELECOME"
p2 = 'pYTHOn iS pROGRAMM'
a = 'python, java, css, html'
a1 = 'this is title part'
print("length of string ", len(p))   #disply lenght of given string
print("Upper Case: ", p.upper())
print("lower case: ",p1.lower())
print("isupper case :", p.isupper())  #check the upper case or not
print("islower case: ", p.islower())  #check lower or not if lower then true
print("Count: ", p.count('o'))
print("SwapCase: ", p2.swapcase())   #swap the upper to lower or lower to upper
print("split string: ",a.split())   #convert string into list
print("Title case: ",a1.title())    #the first character in every word is upper case




#Important functions of math modules

print("\n\n\nMath Modules\n")
from math import *
print(" Sin Value: ",sin(40))
print("Cos Value: ", cos(40))
print("Tan value: ", tan(40))
print("Factorial values: " ,factorial(5))
print ("power value=",pow(5,3))
print("ceil value=",ceil(8888.8888))
print ("Floor value=",floor(8888.8888))
print("Rounded value=",round(8888.8888,3))




