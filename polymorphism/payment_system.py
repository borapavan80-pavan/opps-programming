class payment:
    def pay(self,amount):
        print("payment is successfully")
class creditcard(payment):
    def pay(self,amount):
        print("payment is successfully by a credicard")
class debitcard(payment):
    def pay(self,amount):
        print("payment is successfully by a debitcard")
class upi(payment):
    def pay(self,amount):
        print("payment is successfully by a upi")
class netbanking(payment):
    def pay(self,amount):
        print("payment is successfully by a netbanking")
payment=[creditcard(),debitcard(),upi(),netbanking()]
amount=int(input("enter the amount:"))
choose_one_account=input("choose one account:creditcard,debitcard,upi,netbanking:")
print("you have chosen",choose_one_account)
print("\n------payment methods---\n")
for payments in payment:
    payments.pay(amount)