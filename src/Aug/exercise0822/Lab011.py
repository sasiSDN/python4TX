
name=input("Enter the type manager,Lead or guest ")

match name:
    case "manager"|"lead":
        print("Hello",name)
    case "guest":
        print("Hello guest")
    case _:
        print("Hello there!")