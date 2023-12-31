class BankAccount:

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
   self.__account_number = account_number 

  def __init__(self, account_number, account_holder_name, initial_balance=0.0):
   self.__account_number = account_number 
   self.__account_holder_name = account_holder_name
   self.__account_balance = initial_balance

  def deposit(self , amount):
   if amount > 0:
    self.__account_balance += amount
    print("Deposited rupees is {}. New balance: rupees is {}".format( amount,
self.__account_balance))

   else:
    print("Invalid deposit amount.")

  def withdraw(self, amount):
   if amount > 0 and amount <= self.__account_balance:
    self.__account_balance -= amount
    print("withdrew rupees is{}.New balance:rupees is {}".format(amount,
self.__account_balance))

   else:
    print("Invalid withdraw amount or insufficient balance.")
  
  def display_balance(self):
         print("Account balance for {} (Account #{}): rupees is  {}".format (
        self.__account_holder_name,
self.__account_number,
        self.__account_balance))



account = BankAccount(account_number="12345678",
                       account_holder_name="Nishi",
                         initial_balance=6000.0) 

account.display_balance()
account.deposit(500.0)
account.withdraw(200.0)
account.display_balance()