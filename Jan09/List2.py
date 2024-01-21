#Appending: Merging the data in end of the list:

a=[1,2,3,4,5,6,7,8]

a.append(23)
#print(a)

#extending :
a.extend([23,43])
print(a)


#To get data from keyboard in list manner


l=[]

for i in range(10):
    e=int(input("Enter the value"))
    
    l.append(e)
print(l)

#Add the Element using Slicing
l[1:5]=["Jeeva","Karthick","Rahul","abel"]

print(l)

#Adding the data using indexing
l[6]="Sam"
print(l)

#Removing the data using del,pop,clear,remove

del a[2]

print(a)


