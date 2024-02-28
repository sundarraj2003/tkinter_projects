from tkinter import *
import random
"""
Contions of this Game:

1.First totally 3 options only(stone,paper,siser).
2.The battle rules:
    i)The player select stone:
        1)The computer select paper the player is Win.
        2)The computer select sissor the computer is Win.
        3)The computer select stone the match is Draw.

    ii)The player select paper:
        1)The computer select stone the player is Win.
        2)The computer select sissor the computer is Win.
        3)The computer select paper the match is Draw.

    iii)The player select sissor:
        1)The computer select paper the player is Win.
        2)The computer select stone the computer is Win.
        3)The computer select sissor the match is Draw.
3.This game only played for player and  computer.

"""
#Values
computer_value = {"0": "Stone","1": "Paper","2": "Scissor"}

#Functions
# Reset The Game

def reset_game():
    button_1["state"] = "active"
    button_2["state"] = "active"
    button_3["state"] = "active"
    label_1.config(text="Player              ")
    label_3.config(text="Computer")
    label_4.config(text="Select Next Choice!!!")
 
#Stop the Game
def button_disable():
    button_1["state"] = "disable"
    button_2["state"] = "disable"
    button_3["state"] = "disable"
 
#Player select in Stone 
def select_Stone():
    computer_choice = computer_value[str(random.randint(0, 2))]
    if computer_choice == "Stone":
        match_result = "Match Draw"
    elif computer_choice == "Scissor":
        match_result = "Player Win"
    else:
        match_result = "Computer Win"
    label_4.config(text=match_result)
    label_1.config(text="Stone            ")
    label_3.config(text=computer_choice)
    button_disable()
 
#Player select in paper
def select_paper():
    computer_choice = computer_value[str(random.randint(0, 2))]
    if computer_choice == "Paper":
        match_result = "Match Draw"
    elif computer_choice == "Scissor":
        match_result = "Computer Win"
    else:
        match_result = "Player Win"
    label_4.config(text=match_result)
    label_1.config(text="Paper           ")
    label_3.config(text=computer_choice)
    button_disable()
 
#player select in scissor
def select_scissor():
    computer_choice= computer_value[str(random.randint(0, 2))]
    
    if computer_choice == "Stone":
        match_result = "Computer Win"
    elif computer_choice == "Scissor":
        match_result = "Match Draw"
    else:
        match_result = "Player Win"
    label_4.config(text=match_result)
    label_1.config(text="Scissor         ")
    label_3.config(text=computer_choice)
    button_disable()
 
 
#Tkinter Section(Fround end)
root = Tk()
root.geometry("800x600")
root.title("Stone Paper Scissor Game")
Title=Label(root,text="Stone Paper Scissor",font="normal 40 bold",fg="blue")
Title.pack(pady=20)
frame = Frame(root)
frame.pack()
 
label_1 = Label(frame,text="Player           ",font="italic 20 bold") 
label_2 = Label(frame,text="VS             ",font="normal 20 bold")
label_3 = Label(frame, text="Computer", font="italic 20 bold")
 
label_1.pack(side=LEFT)
label_2.pack(side=LEFT)
label_3.pack(side=LEFT)
 
label_4 = Label(root,text="Select one!!!",font="normal 20 bold",bg="white",width=20,borderwidth=2,relief="solid")
label_4.pack(pady=30)
 
frame1 = Frame(root)
frame1.pack()
 
button_1 = Button(frame1, text="Stone",font=30,height=2, width=15,command=select_Stone)
 
button_2 = Button(frame1, text="Paper ",font=30,height=2, width=15,command=select_paper)
 
button_3 = Button(frame1, text="Scissor",font=30,height=2, width=15,command=select_scissor)
 
button_1.pack(side=LEFT, padx=20,pady=30)
button_2.pack(side=LEFT, padx=20,pady=30)
button_3.pack(padx=20,pady=30)
 
Reset_button=Button(root, text="Reset Game",font="normal 15 bold", fg="white",bg="green", command=reset_game)
Reset_button.pack(pady=40)
root.mainloop()
