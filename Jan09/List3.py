a=[1,2,3,4,5,5]

#a.pop(1)
a.pop()#Last in First out
print(a)


a.remove(1)#element based deleted
print(a)



a.clear()
print(a)


#Sorting

a=["Css","JS","Python","SQL"]

a.sort()

print(a)

b=[1,2,3,4,5,6,7,8]

b.sort(reverse=True)

print(b)

a.sort(reverse=True)

print(a)

#ListComprehension:

#for x in 'set':
 #   for y in 'get':
    #    print(x+y)
    
l=[x+y for x in 'set' for y in 'get' ]

print(l)