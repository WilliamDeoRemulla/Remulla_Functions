food = ["bread=60", "cookie=20", "cake=1000", "chocolate=100", "donut=30", "sandwich=35"]
pick = []

print("Menu: ", food)

def item():
    print("Choose item/s. Type 'stop' to stop")
    while True:
        choose = input("item: ")
        if choose == "bread":
            pick.append(60)
        elif choose == "cookie":
            pick.append(20)
        elif choose == "cake":
            pick.append(1000)
        elif choose == "chocolate":
            pick.append(100)
        elif choose == "donut":
            pick.append(30)
        elif choose == "sandwich":
            pick.append(35)
        elif choose == "stop":
            break

item()


print("Total amount: ", sum(pick))

def pri():
    cash = int(input("Enter payment: "))
    if cash >= sum(pick):
        print("Change: ", cash-sum(pick))
    elif cash < sum(pick):
        print("Please enter valid payment")
        pri()

pri()