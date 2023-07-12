import tkinter
import random

class Game:
    colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown']
    score = 0
    timeleft = 60

    @classmethod
    def nextColour(cls):
        global score
        global timeleft

        if cls.timeleft > 0:
            cls.e.focus_set()

            # Check if the colour typed matches the displayed colour
            if cls.e.get().lower() == cls.colours[1].lower():
                cls.score += 1

            cls.e.delete(0, tkinter.END)
            random.shuffle(cls.colours)
            cls.label.config(fg=str(cls.colours[1]), text=str(cls.colours[0]))
            cls.scoreLabel.config(text="Score: " + str(cls.score))

    @classmethod
    def countdown(cls):
        global timeleft

        if cls.timeleft > 0:
            cls.timeleft -= 1
            cls.timeLabel.config(text="Time left: " + str(cls.timeleft))
            cls.timeLabel.after(1000, cls.countdown)

    @classmethod
    def startGame(cls, event):
        if cls.timeleft == 60:
            cls.countdown()
        cls.nextColour()

    @classmethod
    def main(cls):
        root = tkinter.Tk()
        root.title("Colour game")
        root.geometry("675x300")

        # Add a label for the welcome message
        instructions = tkinter.Label(root, text="WELCOME TO THE COLOUR GAME", font=('Times ', 50, "italic"), fg="purple", bg="pink")
        instructions.pack()

        # Add a label for the instructions
        instructions = tkinter.Label(root, text="Enter the colour of the word displayed", font=('Times', 32, "italic"))
        instructions.pack()

        # Add a label for the score
        cls.scoreLabel = tkinter.Label(root, text="Type anything and press enter to start", font=('Times', 32, "italic"))
        cls.scoreLabel.pack()

        # Add a label for the time left
        cls.timeLabel = tkinter.Label(root, text="Time left: " + str(cls.timeleft), font=('Times', 30, "italic", "bold"))
        cls.timeLabel.pack()

        # Add a label for displaying the colours
        cls.label = tkinter.Label(root, font=('Times', 90, "bold"))
        cls.label.pack()

        # Add an entry box for typing in colours
        cls.e = tkinter.Entry(root, width=30)

        # Bind the startGame function to the Enter key press event
        root.bind('<Return>', cls.startGame)
        cls.e.pack()
        cls.e.focus_set()

        # Start the GUI event loop
        root.mainloop()

if __name__ == '__main__':
    Game.main()
