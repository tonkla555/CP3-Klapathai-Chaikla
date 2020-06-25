from tkinter import *

def leftClickButton(event):
    result = float(textBoxWeight.get()) / (float(textBoxHeight.get()) / 100) ** 2
    lableResult.configure(text=result)
    if result >= 30 :
        lableResultText.configure(text="อ้วนมาก")
    elif result >= 25 :
        lableResultText.configure(text="อ้วน")
    elif result >= 23 :
        lableResultText.configure(text="น้ำหนักเกิน")
    elif result >= 18.6 :
        lableResultText.configure(text="น้ำหนักปกติ เหมาะสม")
    elif result <= 18.5 :
        lableResultText.configure(text="ผอมเกินไป")

mainWindow = Tk()
lableHeight = Label(mainWindow,text="ส่วนสูง (cm.)",bg="#81ecec",fg="#2d3436")
lableHeight.grid(row=0,column=0)
textBoxHeight = Entry(mainWindow,bg="#ffeaa7",fg="#2d3436")
textBoxHeight.grid(row=0,column=1)
lableWeight = Label(mainWindow,text="น้ำหนัก (kg.)",bg="#81ecec",fg="#2d3436")
lableWeight.grid(row=1,column=0)
textBoxWeight = Entry(mainWindow,bg="#ffeaa7",fg="#2d3436")
textBoxWeight.grid(row=1,column=1)
calculateButton = Button(mainWindow,text="คำนวน",bg="#2d3436",fg="#81ecec")
calculateButton.bind('<Button-1>',leftClickButton)
calculateButton.grid(row=2,column=0)
lableResult = Label(mainWindow,text="ผลลัพธ์")
lableResult.grid(row=2,column=1)
lableAnalyze = Label(mainWindow,text="วิเคราห์ :")
lableAnalyze.grid(row=3,column=0)
lableResultText = Label(mainWindow,text="")
lableResultText.grid(row=3,column=1)
mainWindow.mainloop()