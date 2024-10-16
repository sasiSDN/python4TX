a,b,c=(10,32,43)
print(a)
print(b)
print(c)

#search in tuple
cities=("hyderbad","andhrapradesh","yanam")
print("hyderbad" in  cities)
print("chennai" in  cities)


#tuples cannot be appended
#so covert to list and append it  and convert back
lw=(2,4,52)
lis=list(lw)
lis.append(43)
lw=tuple(lis)
print(lw)