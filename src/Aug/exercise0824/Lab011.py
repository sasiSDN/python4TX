#no return type with argument
def print_arguments(*args):
    print(args[0])
    for j in args:
        print(j)

print_arguments("sasi","dhara","naidu",True,20.24,223)
# print_arguments("raina","dhoni")
# print_arguments("Delhi")