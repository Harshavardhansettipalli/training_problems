accounts = {}   

acc_no = int(input("Enter account number: "))
balance = float(input("Enter initial balance: "))
accounts[acc_no] = balance

dep = float(input("\nEnter amount to deposit: "))
accounts[acc_no] += dep
print("Deposit successful!")

withdraw = float(input("Enter amount to withdraw: "))
if withdraw <= accounts[acc_no]:
    accounts[acc_no] -= withdraw
    print("Withdrawal successful!")
else:
    print("Insufficient balance!")

print("\nAccount Balance:", accounts[acc_no])
