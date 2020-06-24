totalPrice = int(input("Total Price :"))
def vatCalculate(totalPrice):
    return totalPrice+(totalPrice*7/100)
print(vatCalculate(totalPrice))