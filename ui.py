from tkinter import *
from brain import TypeBrain
import math
import time

FONT = '#DBF6E9'
THEME = '#0E2431'
SECONDS = 61


class TypingUI:
    """
    Intializes the User Interface of the Typing Test using tkinter

    Contains the title and the favicon
    Creates: -
    Score Label - The value of High Score
    Timer Label - The Timer for the typing test to be conducted
    Result Label - Feedback label to show the CPM, WPM and the word count of the user
    Display Label - Displays the text chosen for the user
    User Input Text box - For the user to type in the text from the Display label
    Start and Reset Button - Start the test and Reset the test
    """

    def __init__(self):
        """
        Initializes the tkinter UI
        """
        self.brain = TypeBrain()
        self.window = Tk()
        self.window.title('Typing Speed Test')
        self.window.iconbitmap('images/icon.ico')
        self.window.config(bg=THEME, padx=20, pady=20)

        self.score = Label(text=f"High Score: {self.brain.score}", bg=THEME, font=('Copperplate Gothic Bold', 15, "bold"), fg='#FF5151')
        self.score.grid(row=1, column=1, pady=2)

        self.timer = Label(text="01:00", bg=THEME, font=('Copperplate Gothic Bold', 20, "bold"), fg='#FF5151')
        self.timer.grid(row=1, column=3, pady=2)

        self.result = Label(text="Press Start to Begin", bg=THEME, font=('Cooper Black', 18, "underline"),
                            fg='#FFD07F')
        self.result.grid(row=2, column=1, columnspan=3, pady=2)

        self.display = Label(text="", bg=THEME, font=('Tahoma', 15,), fg=FONT, wraplength=500, justify="left", )
        self.display.grid(row=3, column=1, columnspan=3, pady=5)

        self.user_input = Text(width=50, height=8, bg=THEME, wrap='word', font=('Tahoma', 15,), fg=FONT,)
        self.user_input.focus()
        self.user_input.grid(row=4, column=1, columnspan=3, pady=10)

        start_icon = PhotoImage(file='images/power.png')
        self.start_button = Button(text="", image=start_icon, compound='top', bg=THEME, bd=0, command=self.start)
        self.start_button.grid(row=5, column=1, pady=2)

        reset_icon = PhotoImage(file='images/reset.png')
        self.reset_button = Button(text="", image=reset_icon, compound='top', bg=THEME, bd=0, command=self.reset,
                                   state='disabled')
        self.reset_button.grid(row=5, column=3, pady=2)

        self.window.mainloop()

    def timer_count(self, timer):
        """
        Function to control the timer seconds every second. Once the timer strikes zero(0) it calls the user_typed
        method to call for calculate and show the result.
        Immediately enables the reset button when the timer hits zero(0)

        :param timer: Takes an integer value of in seconds to be counted from, currently set to 60 secs
        """
        count_min = math.floor(timer / 60)
        count_sec = timer % 60
        if count_sec < 10:
            count_sec = f"0{count_sec}"
        self.timer.config(text=f"0{count_min}:{count_sec}")
        if timer > 0:
            self.window.after(1000, self.timer_count, timer - 1)
        if timer == 0:
            self.user_typed()
            self.reset_button.config(state='normal')

    def start(self):
        """
        Functionality of the START button. This calls the timer_count method to start the typing test.
        Immediately disables the button after pressed.
        """
        self.start_button.config(state='disabled')
        self.result.config(text="")
        self.display.config(text=self.brain.select_stanza())
        self.timer_count(SECONDS)

    def user_typed(self):
        """
        Gathers the data from the Text Box and calls the calculate_result method from the TypeBrain class to pass
        the argument to calculate the result.
        """
        user_data = self.user_input.get("1.0", END)
        final_data = self.brain.calculate_result(user_data=user_data)
        self.result.config(text=f"Total Characters typed: {final_data[2]}\nCorrect Characters typed: {final_data[0]}"
                                f"\nWords per minute: {final_data[1]}")

    def reset(self):
        """
        Function linked with the reset button.
        Destroys the entire UI and recreates it.
        """
        time.sleep(1)
        self.window.destroy()
        TypingUI()
