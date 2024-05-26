L1 = ['HTTP', 'HTTPS', 'FTP', 'DNS']
L2 = [80, 443, 21, 53]

d = {}
for i in range(len(L1)):
    d[L1[i]] = L2[i]

print(d)

def fact (n):
    if n < 0:
        return "Factorial does not exist "
    elif n == 0:
        return 1
    else:
        return n *  fact (n - 1)

num = int(input("Enter a number: "))
result = fact (num)
print(result)

L = ['Network', 'Bio', 'Programming', 'Physics', 'Music']
for i in range(len(L)):
    if L[i].startswith('B'):
        print(L[i])


d = {x: x+1 for x in range(11)}
print(d)


binary = input("Enter a binary number: ")
if not binary.isdigit():
    print("Invalid input. Please enter a binary number.")
else:
    decimal = int(binary, 2)
    print("Decimal equivalent:", decimal)


class BankAccount:
    def _init_(self, account_number, account_holder):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = 0.0

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

class SavingsAccount(BankAccount):
    def _init_(self, account_number, account_holder, interest_rate):
        super()._init_(account_number, account_holder)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest_amount = self.balance * (self.interest_rate / 100)
        self.deposit(interest_amount)

    def _str_(self):
        return f"Balance: {self.balance}, Interest Rate: {self.interest_rate}%"

# Create an instance of BankAccount
bank_acc = BankAccount("123456", "lujain")
bank_acc.deposit(1000)
print(bank_acc.get_balance())
bank_acc.withdraw(500)
print(bank_acc.get_balance())

# Create an instance of SavingsAccount
savings_acc = SavingsAccount("789012", "ahmad", 5)
savings_acc.deposit(2000)
savings_acc.apply_interest()
print(savings_acc)