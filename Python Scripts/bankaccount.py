'''
Created on Apr 20, 2017

@author: jmckay
'''
class BankAccount(object):
    balance = 0
  
    def __init__(self, name):
        self.name = name
    
    def __repr__(self):
        return "This account belongs to %s" % (self.name)
  
    def show_balance(self):
        print "Balance: %.2f" % (self.balance)
  
    def deposit(self, amount):
        if amount <= 0:
            print "Can't deposit empty amount"
            return
        else:
            print "You are depositing %.2f" % (amount)
            self.balance += amount
            self.show_balance()
   
    def withdraw(self, amount):
        if amount > self.balance:
            print "You don't have that much money"
            return
        else:
            print "Withdrawing %.2f..." % (amount)
            self.balance -= amount
            self.show_balance()
      
my_account = BankAccount("TestBank")
print my_account
my_account.show_balance()
my_account.deposit(2000)
my_account.withdraw(1000)
print my_account