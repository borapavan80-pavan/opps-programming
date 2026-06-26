class bankholder:
    def __init__(self,holdername,accountnumber,amount,balanceamount):
        self.holdername=holdername
        self.accountnumber=accountnumber
        self.amount=amount
        self.balanceamount=balanceamount
    def display(self):
        print("holdername:",self.holdername)
        print("accountnumber",self.accountnumber)
        print("amount:",self.amount)
        print("balanceamount:",self.balanceamount)
    def check_balance(self):
        if self.balanceamount>=self.amount:
            print("successful transtion")
        else:
            print("unsuccessful balance")
name=bankholder("pavan",7000,1000,5000)
name.display()
name.check_balance()
name1=bankholder("sai",8000,2000,1000)
name1.display()
name1.check_balance()
name2=bankholder("sri",9000,3000,2000)
name2.display()
name2.check_balance()
