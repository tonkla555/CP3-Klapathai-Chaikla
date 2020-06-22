username = input("Username : ")
password = input("Password : ")
if username == ("tonkla555") and password == ("tonkla55"):
    print("---Welcome To TK-Shop---")
    print("No.    Product   price")
    print("1.     TK-001    (100 THB)")
    print("2.     TK-002    (150 THB)")
    print("3.     TK-002    (200 THB)")
    print("4.     TK-004    (250 THB)")
    No = int(input("Select Product No. : "))
    if No == 1:
        pieces = int(input("Enter the number of pieces : "))
        if pieces > 0 :
            print("-------------------------------Total")
            print("TK-001    100(THB)","*",pieces,"      ",100*pieces,"(THB)")
        else :
            print("You cannot buy 0 items.")
    elif No == 2:
        pieces = int(input("Enter the number of pieces : "))
        if pieces > 0 :
            print("-------------------------------Total")
            print("TK-002    150(THB)","*",pieces,"      ",150*pieces,"(THB)")
        else:
            print("You cannot buy 0 items.")
    elif No == 3:
        pieces = int(input("Enter the number of pieces : "))
        if pieces > 0 :
            print("-------------------------------Total")
            print("TK-003    200(THB)","*",pieces,"      ",200*pieces,"(THB)")
        else:
            print("You cannot buy 0 items.")
    elif No == 4:
        pieces = int(input("Enter the number of pieces : "))
        if pieces > 0 :
            print("-------------------------------Total")
            print("TK-004    250(THB)","*",pieces,"      ",250*pieces,"(THB)")
        else:
            print("You cannot buy 0 items.")
    else :
        print("The item you selected is not available.")
else :
    print("Incorrect Username or Password.")
print("-----Thank You-----")

