#   Import Modules
import tkinter
import random

#   List of possible colors
colors = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Orange', 'White', 'Purple']
score = 0
#   The game time left, initially 60 seconds / 1 min
time = 60
timeleft = time

#   This function starts the game
def startGame(event):
    if timeleft == time:
        countdown()     #   Start the countdown
    nextColor()     #   Run the function to choose the next color

#   Function to choose and display the next color
def nextColor():
    #   Use the globally declared score and variables above
    global score
    global timeleft

    #   If a game is currently in play
    if(timeleft > 0):
        e.focus_set()   #   Make the text entry box active
        if e.get().lower() == colors[1].lower():    #   If the color typed is equal to the color of the text
            score += 1
        e.delete(0, tkinter.END)    #   Clear the text entry box for type the next color
        random.shuffle(colors)
        #   Change the color to type, by changing the text _and_ the color to a random color value
        label.config(fg=str(colors[1]), text=str(colors[0]))
        #   Update the score
        scoreLabel.config(text="Score: " + str(score))

#   Countdown timer function
def countdown():
    global timeleft
    #   If a game is in play
    if timeleft > 0:
        timeleft -= 1   #   Decrement time
        timeLabel.config(text="Time left: " + str(timeleft))    #   Update the time
        timeLabel.after(1000, countdown)    #   Automatically run the function after 1 sec

#   Create a GUI window
top = tkinter.Tk()      #   For details please visit tutorials point
#   Set the title
top.title("Color Game")
#   Set the size
top.geometry("400x250")     #   Width x Length
#   Add an instructions level
instructions = tkinter.Label(top, text="Type in the color of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()

#   Add a score label
scoreLabel = tkinter.Label(top, text="Press enter to start",
                           font=('Helvetica',12))
scoreLabel.pack()

#   Add a time left label
timeLabel = tkinter.Label(top, text="Time left: "+str(timeleft),font=('Helvetica',12))
timeLabel.pack()

#   Add a label for displaying the colors
label = tkinter.Label(top, font = ('Helvetica',60))
label.pack()

#   Add a text entry box for typing in colors
e = tkinter.Entry(top)

#   Run the startgame function when the enter key is pressed
top.bind('<Return>',startGame)
e.pack()

#   Set focus on the entry box
e.focus_set()

#   Copy Right
copyRight = tkinter.Label(top, text="All rights reserved - Muntasher Morshed", font=('Helvetica',12))
copyRight.pack()

#   Start the GUI
top.mainloop()
