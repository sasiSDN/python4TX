#write a program which browser wants to run automation
browser_name=input("Enter the browser name:\n")
browser_name=browser_name.lower()
match browser_name:
    case "chrome":
        if browser_name=="chrome":
            print("Hello Chrome")
        print("Execute the chrome code")
    case "edge":
        print("Execute the edge code")
    case "firefox":
        print("Execute the firefox code")
    case "safari":
        print("Execute the safari code")
    case _:
        print("Browser not found")
