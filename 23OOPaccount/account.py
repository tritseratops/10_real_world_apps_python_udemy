class Account:

    balance = 0

    class_var = 0


    def __init__(self, file_path):
        with open(file_path, 'r') as file:
            self.balance = int(file.read())
            self.file_path = file_path

    def withdraw(self, amount):
        self.balance =self.balance-amount

    def deposit(self, amount):
        self.balance =self.balance+amount
        Account.class_var = self.balance

    def commit(self):
        with open(self.file_path, 'w') as file:
            file.write(str(self.balance))


class Checking(Account):

    def __init__(self, file_path, fee):
        Account.__init__(self, file_path)
        self.fee = fee


    def transfer(self, amount):
        self.balance = self.balance - amount - self.fee

# account = Checking("balance.txt",1)

# print(account.balance)
# account.transfer(100)
# print(account.balance)
# # account.deposit(200)
# # print(account.balance)
# account.commit()
# account2= Account("balance.txt")
# print(account2.balance)
# account.transfer(100)
# print(account.balance)
# print(account2.balance)

account = Account("balance.txt")
account2 = Account("balance.txt")
print(account.class_var)
print(account2.class_var)
account.deposit(200)
print(account.class_var)
print(account2.class_var)