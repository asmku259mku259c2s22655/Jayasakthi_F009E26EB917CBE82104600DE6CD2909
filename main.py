#challenge 2.1
class BankAccount:
  def_init_(self,account_number,account_holder_name,initial_balance=0.0):
self._account_number=account_number
self._account_holder_name=account_holder_name
self._account_balance=initial_balance
def deposit(self,amount):
  if amount>0:
    self._account_balance+=amount
    #self_account_balance=self._account_balance +amount
    print("Deposited ${}.New balance:${}".format(amount,self._account_balance))
  else:
    print("Invalid deposit amount.please depoist a positive amount.")
    def withdraw(self,amount):
      if amount>0 and amount<=self._account_balance:
        self._account_balance_=amount
        #self._account_balance=self._account_balance_amount
        print("withdrew ${}.New balance:${}".format(amount,self._accpunt_balance))
      else:
        print("Invalis withdrawal amount or insufficent balance.")
        def display_balance(self):
          print("Account balance for{}(account#{}):${}".format(self._account_holder_name,self._account_balance))
          #create an instance of the bank account class
account=BankAccount(account_number="12345678",account_holder_name="Rithu",initial_balance=5000.0)
#Test deposit and withdrawal functionality
account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account display_balance()

        