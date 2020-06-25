systemMenu = {'ข้าวมันไก่':40,'ข้าวหมูแดง':40,'ข้าวหมูกรอบ':50,'ข้าวหน้าเป็ด':50}
menuList = []
def showBill():
    print("---- My Food ----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number][0],menuList[number][1])
        totalPrice += int(menuList[number][1])
    return totalPrice

while True:
    menuName = input("Please Enter Menu :")
    if(menuName.lower() == "exit"):\
        break
    else:
        menuList.append([menuName,systemMenu[menuName]])

print("Total Price : ",showBill())