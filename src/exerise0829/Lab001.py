#List- collection of items

list=[1,2,3,4]
#list2=[1,"sasi",132.2]
print(list)
print(len(list))

print(list[0])
print(list[2])


#indexing
list[0]="sasi"
print(list[0])
print(list)

for j in list:
    print(j)






list.append(5)
print(list)
list.extend([6,7,8,9])
list.extend(["naidu","kinng"])
list.insert(1,"naidu")
list[1]="king"
list.insert(-1,"Sasi")
list.remove("kinng")
print(list)


##########
copy_list=list.copy()
print(copy_list)
list.remove("naidu")
# list.sort()
print(list)


l1=[1,2,5]
l2=[2,4,6]
l3=l1+l2
print(l3)


sas=[2,5,3,6,3,6]
# sas.sort()
# print(sas)
# sas.reverse()
sas.sort(reverse=False)
print(sas)