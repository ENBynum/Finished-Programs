from tkinter import *
from customtkinter import *
from math import *

# System Settings
set_appearance_mode("System")
set_default_color_theme("blue")

# Create App Window
app = CTk()
app.geometry("600x800")
for i in range(1,23):
    app.rowconfigure(index = i, minsize=50, uniform="a")
for i in range(0,1):
    app.columnconfigure(index = i, minsize=600, uniform="b")
app.propagate(False)

appLabel = CTkLabel(app, text="Point of Sales Calculator", font=("Arial", 36, "bold")).grid(row=0, column=0, padx=12, pady=12)



# Add Cost Frame
costFrame = CTkFrame(app, width=400, height=240, border_width=3)
for i in range(0,4):
    costFrame.rowconfigure(index=i, minsize=60, uniform="c")
for i in range(0,3):
    costFrame.columnconfigure(index=i, minsize=133, uniform="d")
costFrame.propagate(False)    
costFrame.grid(row=1, column=0, rowspan=5)

costFrameLabel = CTkLabel(costFrame, text="Purchase Information", font=("Arial", 24, "bold")).grid(row=0, column=0, columnspan=3)

amountDueLabel = CTkLabel(costFrame, text="Amount Due:", font=("Arial", 14)).grid(row=1, column=0, sticky="e")
amountDue = CTkEntry(costFrame, height=50, width=220, font=("Arial", 14))
amountDue.grid(row=1, column=1, columnspan=2)

amountReceivedLabel = CTkLabel(costFrame, text="Amount Received:", font=("Arial", 14)).grid(row=2, column=0, sticky="e")
amountReceived = CTkEntry(costFrame, height=50, width=220, font=("Arial", 14))
amountReceived.grid(row=2, column=1, columnspan=2)

change = 0
def getChangeDue():
    global change

    cost = float(amountDue.get())
    print(cost)
    paid = float(amountReceived.get())
    print(paid)

    if paid < cost:
        changeDueLabel.configure(text="Insufficient Funds", font=("Arial", 18, "bold"))
    elif paid == cost:
        changeDueLabel.configure(text="No Change Due", font=("Arial", 18, "bold"))
    elif (paid - cost) < 1:
        change = paid - cost
        changeDueLabel.configure(text="Change Due: ${:0.2f}".format(change), font=("Arial", 18, "bold",))
        changeDue()
        amountDue.delete(0, END)
        amountReceived.delete(0, END)
        amountDue.focus()
    else:
        change = paid - cost
        changeDueLabel.configure(text="Change Due: ${:.2f}".format(change), font=("Arial", 18, "bold",))
        changeDue()
        amountDue.delete(0, END)
        amountReceived.delete(0, END)
        amountDue.focus()

submitButton = CTkButton(costFrame, height=40, width=100, text="Submit", font=("Arial", 18, "bold"), command=getChangeDue).grid(row=3, column=0,columnspan=3)



# Add Change Due Frame
changeDueFrame = CTkFrame(app, width=400, height=400, border_width=3)
for i in range(0,10):
    changeDueFrame.rowconfigure(index=i, minsize=40, uniform="e")
for i in range(0,3):
    changeDueFrame.columnconfigure(index=i, minsize=100, uniform="f")
changeDueFrame.propagate(False)
changeDueFrame.grid(row=6, column=0, rowspan=9)

changeDueLabel = CTkLabel(changeDueFrame, text="", font=("Arial", 24, "bold"))
changeDueLabel.grid(row=0, column=0, rowspan=2, columnspan=3)

def changeDue():
    global change

    twenties = floor(change / 20)
    change = round(change % 20, 2)
    print("After Twenties: {}".format(change))
    twentyDue.configure(text=twenties)
    twentyTotal.configure(text="${}".format(twenties * 20))

    tens = floor(change / 10)
    change = round(change % 10, 2)
    print("After Tens: {}".format(change))
    tenDue.configure(text=tens)
    tenTotal.configure(text="${}".format(tens * 10))

    fives = floor(change / 5)
    change = round(change % 5, 2)
    print("After Fives: {}".format(change))
    fiveDue.configure(text=fives)
    fiveTotal.configure(text="${}".format(fives * 5))

    ones = floor(change / 1)
    change = round(change % 1, 2)
    print("After Ones: {}".format(change))
    oneDue.configure(text=ones)
    oneTotal.configure(text="${}".format(ones))

    quarters = floor(change / 0.25)
    change = round(change % 0.25, 2)
    print("After Quarters: {}".format(change))
    quarterDue.configure(text=quarters)
    quarterTotal.configure(text="${:0.2f}".format(quarters * 0.25))

    dimes = floor(change / 0.10)
    change = round(change % 0.10, 2)
    print("After Dimes: {}".format(change))
    dimeDue.configure(text=dimes)
    dimeTotal.configure(text="${:0.2f}".format(dimes * 0.10))

    nickels = floor(change / 0.05)
    change = round(change % 0.05, 2)
    print("After Nickels: {}".format(change))
    nickelDue.configure(text=nickels)
    nickelTotal.configure(text="${:0.2f}".format(nickels * 0.05))

    pennies = floor(change / 0.01)
    change = round(change % 0.01, 2)
    print("After Pennies: {}".format(change))
    pennyDue.configure(text=pennies)
    pennyTotal.configure(text="${:0.2f}".format(pennies * 0.01))

twentyDueLabel = CTkLabel(changeDueFrame, text="$20 Bills: ", font=("Arial", 14,"bold")).grid(row=2, column=0, sticky="ne")
twentyDue = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
twentyDue.grid(row=2, column=1, padx=10, sticky="nw")
twentyTotal = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
twentyTotal.grid(row=2, column=2, sticky="nw")

tenDueLabel = CTkLabel(changeDueFrame, text="$10 Bills: ", font=("Arial", 14,"bold")).grid(row=3, column=0, sticky="ne")
tenDue = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
tenDue.grid(row=3, column=1, padx=10, sticky="nw")
tenTotal = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
tenTotal.grid(row=3, column=2, sticky="nw")

fiveDueLabel = CTkLabel(changeDueFrame, text="$5 Bills: ", font=("Arial", 14,"bold")).grid(row=4, column=0, sticky="ne")
fiveDue = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
fiveDue.grid(row=4, column=1, padx=10, sticky="nw")
fiveTotal = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
fiveTotal.grid(row=4, column=2, sticky="nw")

oneDueLabel = CTkLabel(changeDueFrame, text="$1 Bills: ", font=("Arial", 14,"bold")).grid(row=5, column=0, sticky="ne")
oneDue = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
oneDue.grid(row=5, column=1, padx=10, sticky="nw")
oneTotal = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
oneTotal.grid(row=5, column=2, sticky="nw")

quarterDueLabel = CTkLabel(changeDueFrame, text="Quarters: ", font=("Arial", 14,"bold")).grid(row=6, column=0, sticky="ne")
quarterDue = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
quarterDue.grid(row=6, column=1, padx=10, sticky="nw")
quarterTotal = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
quarterTotal.grid(row=6, column=2, sticky="nw")

dimeDueLabel = CTkLabel(changeDueFrame, text="Dimes: ", font=("Arial", 14,"bold")).grid(row=7, column=0, sticky="ne")
dimeDue = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
dimeDue.grid(row=7, column=1, padx=10, sticky="nw")
dimeTotal = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
dimeTotal.grid(row=7, column=2, sticky="nw")

nickelDueLabel = CTkLabel(changeDueFrame, text="Nickels: ", font=("Arial", 14,"bold")).grid(row=8, column=0, sticky="ne")
nickelDue = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
nickelDue.grid(row=8, column=1, padx=10, sticky="nw")
nickelTotal = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
nickelTotal.grid(row=8, column=2, sticky="nw")

pennyDueLabel = CTkLabel(changeDueFrame, text="Pennies: ", font=("Arial", 14,"bold")).grid(row=9, column=0, sticky="ne")
pennyDue = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
pennyDue.grid(row=9, column=1, padx=10, sticky="nw")
pennyTotal = CTkLabel(changeDueFrame, text="", font=("Arial", 14))
pennyTotal.grid(row=9, column=2, sticky="nw")

# Run App
app.mainloop()