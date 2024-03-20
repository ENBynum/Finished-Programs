import tkinter
import customtkinter
import random
import threading
import time

# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Adding App Window
app = customtkinter.CTk()
app.geometry("500x500")
app.title("Rock, Paper, Scissors, Shoot!")
titleIcon = tkinter.PhotoImage("C:\\Users\\emman_7z18d6d\\OneDrive\\Documents\\GitHub\\Learning-Python\\images\\RPS.png")
app.iconphoto = titleIcon

# Adding Main Title
title = customtkinter.CTkLabel(app, text="Let's play a game of Rock, Paper, Scissors!", font=("Arial", 22, "bold"))
title.pack(pady=11)

# Adding Player Choice Frame
playerWins = 0
compWins = 0
ties = 0

playerFrame = customtkinter.CTkFrame(app, height=100, width=300, border_width=2)
playerFrame.pack(pady=12)
for i in range(0,3):
    playerFrame.rowconfigure(index=i, minsize=33, uniform="a")
for i in range(0,3):
    playerFrame.columnconfigure(index=i, minsize=100, uniform="a")
playerFrame.grid_propagate(False)

    # Adding Frame Label
playerFrameLabel = customtkinter.CTkLabel(playerFrame, text="Make a Choice", font=("Arial", 18, "bold"))
playerFrameLabel.grid(row=0, column=0, columnspan=3, sticky="s")

    # Adding Rock Button
def playerRock():
    global playerWins
    global compWins
    global ties

    choices = ["Rock", "Paper", "Scissors"]
    compChoice = random.choice(choices)

    if compChoice == "Rock":
        ties += 1
        roundResult.configure(text = "It's a tie!")
        currentChoices.configure(text = "Player's Choice: Rock     Computer's Chioce: {}".format(compChoice))
        winCounter.configure(text = "Player Wins: {}    Computer Wins: {}     Ties: {}".format(playerWins, compWins, ties))
    elif compChoice == "Paper":
        compWins += 1
        roundResult.configure(text = "You've lost this round!")
        currentChoices.configure(text = "Player's Choice: Rock     Computer's Chioce: {}".format(compChoice))
        winCounter.configure(text = "Player Wins: {}    Computer Wins: {}     Ties: {}".format(playerWins, compWins, ties))
    elif compChoice == "Scissors":
        playerWins += 1
        roundResult.configure(text = "You've won this round!")
        currentChoices.configure(text = "Player's Choice: Rock     Computer's Chioce: {}".format(compChoice))
        winCounter.configure(text = "Player Wins: {}    Computer Wins: {}     Ties: {}".format(playerWins, compWins, ties))
    if playerWins == 5 or compWins == 5:
        rockButton.configure(state=tkinter.DISABLED)
        paperButton.configure(state=tkinter.DISABLED)
        scissorsButton.configure(state=tkinter.DISABLED)
    if playerWins == 5:
        winDisplay.configure(text = "You've Won!!!")
    if compWins == 5:
        winDisplay.configure(text = "You've Lost!")

rockButton = customtkinter.CTkButton(playerFrame, height=30, width=75, text="Rock", font=("Arial", 8), command=playerRock)
rockButton.grid(row=1, column=0, rowspan=2)
    # Adding Paper Buttons
def playerPaper():
    global playerWins
    global compWins
    global ties

    choices = ["Rock", "Paper", "Scissors"]
    compChoice = random.choice(choices)

    if compChoice == "Paper":
        roundResult.configure(text = "It's a tie!")
        ties += 1
        currentChoices.configure(text = "Player's Choice: Paper     Computer's Chioce: {}".format(compChoice))
        winCounter.configure(text = "Player Wins: {}    Computer Wins: {}     Ties: {}".format(playerWins, compWins, ties))
    elif compChoice == "Scissors":
        roundResult.configure(text = "You've lost this round!")
        compWins += 1
        currentChoices.configure(text = "Player's Choice: Paper     Computer's Chioce: {}".format(compChoice))
        winCounter.configure(text = "Player Wins: {}    Computer Wins: {}     Ties: {}".format(playerWins, compWins, ties))
    elif compChoice == "Rock":
        roundResult.configure(text = "You've won this round!")
        playerWins += 1
        currentChoices.configure(text = "Player's Choice: Paper     Computer's Chioce: {}".format(compChoice))
        winCounter.configure(text = "Player Wins: {}    Computer Wins: {}     Ties: {}".format(playerWins, compWins, ties))
    if playerWins == 5 or compWins == 5:
        rockButton.configure(state=tkinter.DISABLED)
        paperButton.configure(state=tkinter.DISABLED)
        scissorsButton.configure(state=tkinter.DISABLED)
    if playerWins == 5:
        winDisplay.configure(text = "You've Won!!!")
    if compWins == 5:
        winDisplay.configure(text = "You've Lost!")

paperButton = customtkinter.CTkButton(playerFrame, height=30, width=75, text="Paper", font=("Arial", 8), command=playerPaper)
paperButton.grid(row=1, column=1, rowspan=2)
    # Adding Scissors Buttons
def playerScissors():
    global playerWins
    global compWins
    global ties

    choices = ["Rock", "Paper", "Scissors"]
    compChoice = random.choice(choices)

    if compChoice == "Scissors":
        roundResult.configure(text = "It's a tie!")
        ties += 1
        currentChoices.configure(text = "Player's Choice: Scissors     Computer's Chioce: {}".format(compChoice))
        winCounter.configure(text = "Player Wins: {}    Computer Wins: {}     Ties: {}".format(playerWins, compWins, ties))
    elif compChoice == "Rock":
        roundResult.configure(text = "You've lost this round!")
        compWins += 1
        currentChoices.configure(text = "Player's Choice: Scissors     Computer's Chioce: {}".format(compChoice))
        winCounter.configure(text = "Player Wins: {}    Computer Wins: {}     Ties: {}".format(playerWins, compWins, ties))
    elif compChoice == "Paper":
        roundResult.configure(text = "You've won this round!")
        playerWins += 1
        currentChoices.configure(text = "Player's Choice: Scissors     Computer's Chioce: {}".format(compChoice))
        winCounter.configure(text = "Player Wins: {}    Computer Wins: {}     Ties: {}".format(playerWins, compWins, ties))
    if playerWins == 5 or compWins == 5:
        rockButton.configure(state=tkinter.DISABLED)
        paperButton.configure(state=tkinter.DISABLED)
        scissorsButton.configure(state=tkinter.DISABLED)
    if playerWins == 5:
        winDisplay.configure(text = "You've Won!!!")
    if compWins == 5:
        winDisplay.configure(text = "You've Lost!")

scissorsButton = customtkinter.CTkButton(playerFrame, height=30, width=75, text="Scissors", font=("Arial", 8), command=playerScissors)
scissorsButton.grid(row=1, column=2, rowspan=2)



# Adding Win/Lose Display Frame
winDisplay = customtkinter.CTkLabel(app, text="", font=("Arial", 24, "bold"))
winDisplay.pack(pady=9)



# Adding Results Frame
resultsFrame = customtkinter.CTkFrame(app, height=250, width=400, border_width=2)
resultsFrame.pack(pady=12)
for i in range(0,3):
    resultsFrame.rowconfigure(index=i, minsize=50, uniform="a")
resultsFrame.columnconfigure(index=0, minsize=400, uniform="a")
resultsFrame.grid_propagate(False)
    # Adding Frame Label
resultsFrameLabel = customtkinter.CTkLabel(resultsFrame, text="Results", font=("Arial", 18, "bold"))
resultsFrameLabel.grid(row=0, column=0)
    # Adding Round Result Label
roundResult = customtkinter.CTkLabel(resultsFrame, text="", font=("Arial", 12))
roundResult.grid(row=1, column=0, sticky="s")
    # Adding Current Choices Label
currentChoices = customtkinter.CTkLabel(resultsFrame, text="", font=("Arial", 12))
currentChoices.grid(row=2, column=0)
    # Adding Win Counter Label
winCounter = customtkinter.CTkLabel(resultsFrame, text="", font=("Arial", 12))
winCounter.grid(row=3, column=0, sticky="n")



# Running Main Loop
app.mainloop()