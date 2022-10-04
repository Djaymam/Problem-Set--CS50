
cash = float(input("Change: "))

change = int(cash*100)

print("Your change is :" + str(cash)+"$")

if change >= 25:
    coin25 = change/25
    change = change % 25
    print(int(coin25), end=" ")
    print(" coin of 25¢ Quarters! ")

if change >= 10:
    coin10 = change/10
    change = change % 10
    print(int(coin10), end=" ")
    print("coin of 10¢ Dimes!")

if change >= 5:
    coin5 = change / 5
    change = change % 5
    print(int(coin5), end=" ")
    print("coin of 5¢ Nickels!")

if change >= 1:
    coin1 = change / 1
    print()
    print(int(coin1), end=" ")
    print("coin of 1¢ Pennies!")


