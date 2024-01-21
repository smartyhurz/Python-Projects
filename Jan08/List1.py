#how to create a list:

a=[10,20,30,40]

print(a)

#Second way of List Creation:

a=list([1,2,3,4,5])
print(a)

#Different Types of Data's

b=[1,"Jeeva",8.0,"Fair",'M']

print(b)

#Nested List Creation

h=[1,2,[4.5,"jeeva"]]

print(h)

#Indexing

print(a[0])

#Nested List Index:

print(h[2][1])

#Reversing Index:

a=[1,2,3,4,5,6,7,8,9,10]

print(a[-4])

print(a[4])


#Slicing:

'''Retrieval data for range of things'''


#[start:stop:step]


print(a[1:4])

print(a[2:])  #retrieval the data for a range of thing should be start on 2 indext to entire data

print(a[:2])  #Print the data for a range of things shoule be started only first 2 data

print(a[-1:]) #Reverse indexing and slicing is possible

print(a[:-4])

print(a[-6:-1])


#Repetition:

a=[1,2,3]
print(a*2)

#Iterating:

'''its called one by one printing'''

a=[1,2,3,4,5,6,7,8,9,10]

for i in a:
    print(i)
    
courses=["Java","Python","Php","Perl","Ruby"]

for j in courses:
    print("The Programming language is:",j)
    
# Sum of List of elements

sum=0

for i in a:
    sum=sum+i
print("The of the List eleement is:",sum)
 

#Even Number Printing:

for i in a:
    if i%2==0:
        print(i)

#Exercises:
a=["jeeva","Rahul","Arun","Vimal"]

for i in a:
    print(i,"is a Studying Itvedant")
