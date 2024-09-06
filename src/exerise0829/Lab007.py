set1={1,2,3}
set2={4,5,6}
set=set1.union(set2)
print(set)


set1={1,2,3,4,5}
set2={4,5,6}
set=set1.intersection(set2)
print(set)

set1=set1.difference(set2) # {1, 2, 3} it will remove duplicates and set2
print(set1)
set1={1,2,3,4,5}
set2={4,5,6}
set3=set2.difference(set1)
print(set3)

set1={1,2,3,4,5,6}
set2={4,5,6}
set3=set2.issubset(set1)
print(set3)