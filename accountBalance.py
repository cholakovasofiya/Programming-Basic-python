balance = 0
command = input()
while command != "NoMoreMoney":
    deposit = float(command)

    if deposit < 0:
        print("Invalid operation!")
        break
    command = input()
    balance += deposit
    print(f"Increase: {deposit:.2f}")
print(f"Total: {balance:.2f}")
