
my_shopping=["bread","Milk","Biscuit"]
print(my_shopping)
print(my_shopping[0])
print(len(my_shopping))


def more_item(my_list):
    # my_list.append("choclate")
    new_item=input("Enter new item\n")
    my_list.append(new_item)
    # my_shopping.remove(new_item)
    my_list.insert(0,new_item)
    print(my_list)



more_item(my_shopping)