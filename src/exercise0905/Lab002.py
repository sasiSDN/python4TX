class Bank:
    def __init__(self,account_number,balance):
        self.__account_number=account_number
        self.balance=balance

    def depoist(self,amount):
        self.balance=self.balance+amount
    def check_balance(self):
        print(self.balance)
    def show_account_number(self,is_auth):
        if is_auth==True:
            print(self.__account_number)
        else:
            print("Not authorized")
HDFC=Bank(324224242,1000)
HDFC.depoist(100)
HDFC.check_balance()
HDFC.show_account_number(False)