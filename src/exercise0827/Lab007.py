
#Decorators

#Decorators are two parts
#wrapper & call
def Before_ui_after_ui(fun):
    def wap2():
        print("Before the UI test")
        print("Start the browser")
        fun()
        print("Ending  the UI test")
        print("Quit the browser")
    return wap2()
@Before_ui_after_ui
def test():
    print("Im doing ui test")