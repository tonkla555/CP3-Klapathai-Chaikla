menuList = []
priceList = []
def showBill():
    print("---- My Food ----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number])
        totalPrice += int(priceList[number])
    return totalPrice

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):\
        break
    else:
        menuPrice = input("Price :")
        menuList.append(menuName)
        priceList.append(menuPrice)

print("Total Price :",showBill())