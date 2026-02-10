balance = int(input("enter your balance: "))
withdrawal = int(input("enter your withdrawl amount: "))
verification_status = input("enter verification status true/false: ")

if verification_status == "true":
    verification_status = True
elif verification_status == "false":
    verification_status = False
else:
    print("enter valid input")
    exit()

if verification_status and withdrawal <= balance:
    print("Withdrawal successful!")
elif not verification_status:
    print("you're not verified")
else:
    print("insufficient balance")
