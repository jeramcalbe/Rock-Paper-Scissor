from tkinter import *
from PIL import ImageTk, Image
import random


BACKGROUND_COLOR = 'yellow'
FRAME_FONT = ('Times', 15, 'bold')
BUTTONS_FONT = ('Times', 10, 'bold')
LABEL_FONT = ('Times', 13, 'bold')
BORDER_WIDTH = 0


# FUNCTIONS
def button_press(button):
    global player_score
    global computer_score
    global score_limit

    player_text.set(button)
    buttons = ['ROCK', 'PAPER', 'SCISSOR']
    computer = random.choice(buttons)
    computer_text.set(computer)
    buttons_status = [player_rock_button, player_paper_button, player_scissor_button]
    if player_text.get() == computer_text.get():
        game_result.set('TIE!')
    elif (player_text.get() == 'ROCK' and computer_text.get() == 'SCISSOR') or \
         (player_text.get() == 'PAPER' and computer_text.get() == 'ROCK') or \
         (player_text.get() == 'SCISSOR' and computer_text.get() == 'PAPER'):
        game_result.set('YOU WIN!')
        player_score.set(player_score.get() + 1)
        if player_score.get() == score_limit.get():
            game_result.set('GAME OVER!\nYOU WIN!')
            for button in buttons_status:
                button.config(state=DISABLED)
    else:
        game_result.set('COMPUTER WINS')
        computer_score.set(computer_score.get() + 1)
        if computer_score.get() == score_limit.get():
            game_result.set('GAME OVER!\nCOMPUTER WINS')
            for button in buttons_status:
                button.config(state=DISABLED)


def button_restart():
    text = [player_text, game_result, computer_text]
    buttons_status = [player_rock_button, player_paper_button, player_scissor_button]
    scores = [player_score, computer_score]
    score_limit.set(0)
    score_limit_entry.insert(1, str(5))

    for command in text:
        command.set('')
        for button in buttons_status:
            button.config(state=ACTIVE)
            for score in scores:
                score.set(0)


# Window
window = Tk()
window.title('ROCK_PAPER_SCISSOR')
window.resizable(False, False)
window.config(bg=BACKGROUND_COLOR)

player_text = StringVar()
computer_text = StringVar()
game_result = StringVar()
score_limit = IntVar()

# Resized Button images
rock = Image.open('Button Images/stone.png')
scissor = Image.open('Button Images/scissors.png')
paper = Image.open('Button Images/paper.png')
restart = Image.open('Button Images/restart.png')

rock_resized = rock.resize((50, 50))
scissor_resized = scissor.resize((50, 50))
paper_resized = paper.resize((50, 50))
restart_resized = restart.resize((25, 25))

# Newly Resized Button images
rocks = ImageTk.PhotoImage(rock_resized)
scissors = ImageTk.PhotoImage(scissor_resized)
papers = ImageTk.PhotoImage(paper_resized)
restarts = ImageTk.PhotoImage(restart_resized)

# FRAME
window_frame = Frame(window, bg=BACKGROUND_COLOR)
window_frame.pack(padx=10, pady=10)

# PLAYERS FRAME
player_frame = LabelFrame(window_frame, text='PLAYER', font=FRAME_FONT,
                          bg=BACKGROUND_COLOR, labelanchor='n')
player_frame.pack(anchor='n')

# SCORE LIMIT FRAME

score_limit_frame = LabelFrame(player_frame, text='Score Limit', font=('Arial', 6, 'bold'),
                               bg=BACKGROUND_COLOR, labelanchor='n', width=55, height=35)
score_limit_frame.grid(row=4, column=0, pady=1)

score_limit_entry = Entry(score_limit_frame, textvariable=score_limit, font=('Times', 8, 'bold'),
                          bg=BACKGROUND_COLOR, width=5)
score_limit_entry.insert(1, str(5))
score_limit_entry.pack()

# PLAYERS CHOICE
match_frame1 = LabelFrame(window_frame, text='Players Choice', width=215, height=50, bg=BACKGROUND_COLOR)
match_frame1.pack(anchor='n', padx=3, pady=3)
players_choice_label = Label(match_frame1, textvariable=player_text, width=29, height=2, font=BUTTONS_FONT)
players_choice_label.pack()

# MATCH RESULT
match_result = LabelFrame(window_frame, width=215, height=50, bg=BACKGROUND_COLOR,
                          labelanchor='n',)
match_result.pack(anchor='n')
result_label = Label(match_result, textvariable=game_result, width=17, height=2, font=FRAME_FONT)
result_label.pack()

# COMPUTERS CHOICE
match_frame2 = LabelFrame(window_frame, text='Computers Choice', width=215, height=50, bg=BACKGROUND_COLOR,
                          labelanchor='se')
match_frame2.pack(anchor='n', padx=2, pady=2)
computers_choice_label = Label(match_frame2, textvariable=computer_text, width=29, height=2, font=BUTTONS_FONT)
computers_choice_label.pack()


# COMPUTERS FRAME
computers_frame = LabelFrame(window_frame, text='COMPUTER', font=FRAME_FONT,
                             bg=BACKGROUND_COLOR, labelanchor='s')
computers_frame.pack(anchor='n')


# PLAYERS SCORE LABELS
player_score = Label(player_frame, text='Your Score: ', bg=BACKGROUND_COLOR, font=LABEL_FONT)
player_score.grid(row=2, column=0, columnspan=3)
# PLAYER SCORE
player_score = IntVar()
display_player_score = Label(player_frame, textvariable=player_score, width=10, bg=BACKGROUND_COLOR)
display_player_score.grid(row=3, column=0, columnspan=3)

# PLAYERS BUTTONS
player_rock_button = Button(player_frame, text='ROCK', image=rocks, compound='top',
                            relief=RIDGE,
                            font=BUTTONS_FONT,
                            bg=BACKGROUND_COLOR,
                            activebackground=BACKGROUND_COLOR,
                            command=lambda: button_press('ROCK'),
                            borderwidth=BORDER_WIDTH)
player_rock_button.grid(row=0, column=0, padx=5, pady=3)

player_paper_button = Button(player_frame, text='PAPER', image=papers, compound='top',
                             relief=RIDGE,
                             font=BUTTONS_FONT,
                             bg=BACKGROUND_COLOR,
                             activebackground=BACKGROUND_COLOR,
                             command=lambda: button_press('PAPER'),
                             borderwidth=BORDER_WIDTH)
player_paper_button.grid(row=0, column=1, padx=5, pady=3)

player_scissor_button = Button(player_frame, text='SCISSOR', image=scissors, compound='top',
                               relief=RIDGE,
                               font=BUTTONS_FONT,
                               bg=BACKGROUND_COLOR,
                               activebackground=BACKGROUND_COLOR,
                               command=lambda: button_press('SCISSOR'),
                               borderwidth=BORDER_WIDTH)
player_scissor_button.grid(row=0, column=2, padx=5, pady=3)

# COMPUTERS SCORE LABELS
computer_score = Label(computers_frame, text='Computer Score: ', bg=BACKGROUND_COLOR, font=LABEL_FONT)
computer_score.grid(row=1, column=0, columnspan=3)
# COMPUTER SCORE
computer_score = IntVar()
display_computer_score = Label(computers_frame, textvariable=computer_score, width=13, bg=BACKGROUND_COLOR)
display_computer_score.grid(row=0, column=0, columnspan=3)

# COMPUTERS BUTTONS
rock_button = Label(computers_frame, text='ROCK', image=rocks, compound='top',
                    relief=RIDGE,
                    font=BUTTONS_FONT,
                    bg=BACKGROUND_COLOR,
                    activebackground=BACKGROUND_COLOR,
                    borderwidth=BORDER_WIDTH)
rock_button.grid(row=2, column=0, padx=5, pady=3)

paper_button = Label(computers_frame, text='PAPER', image=papers, compound='top',
                     relief=RIDGE,
                     font=BUTTONS_FONT,
                     bg=BACKGROUND_COLOR,
                     activebackground=BACKGROUND_COLOR,
                     borderwidth=BORDER_WIDTH)
paper_button.grid(row=2, column=1, padx=5, pady=3)

scissor_button = Label(computers_frame, text='SCISSOR', image=scissors, compound='top',
                       relief=RIDGE,
                       font=BUTTONS_FONT,
                       bg=BACKGROUND_COLOR,
                       activebackground=BACKGROUND_COLOR,
                       borderwidth=BORDER_WIDTH)
scissor_button.grid(row=2, column=2, padx=5, pady=3)

restart_button = Button(player_frame, image=restarts,
                        relief=RIDGE,
                        font=BUTTONS_FONT,
                        bg=BACKGROUND_COLOR,
                        activebackground=BACKGROUND_COLOR,
                        highlightcolor=BACKGROUND_COLOR,
                        command=lambda: button_restart(),
                        borderwidth=BORDER_WIDTH)
restart_button.grid(row=4, column=0, columnspan=3, pady=3)

window.wm_attributes('-toolwindow', True)
window.mainloop()
