from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 30
s_rounds = 0
timer_set = None
# ---------------------------- TIMER RESET ------------------------------- # 
def time_reset():
    if label_timer['text'] == 'Timer':
        return None
    window.after_cancel(timer_set)
    canvas.itemconfig(canvas_text, text='00:00')
    label_timer.config(text='Timer')
    label_check.config(text='')
    global s_rounds
    s_rounds = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_clicked():
    lbm = LONG_BREAK_MIN * 60
    sbm = SHORT_BREAK_MIN * 60
    wm = WORK_MIN * 60
    global s_rounds
    s_rounds += 1
    if s_rounds % 8 == 0:
        count_down(lbm)
        label_timer.config(text='Big Break', fg=RED)
    elif s_rounds % 2 == 0:
        count_down(sbm)
        label_timer.config(text=f'Break {int(s_rounds/2)}', fg=PINK)
    else:
        count_down(wm)
        label_timer.config(text=f'Work {int(math.floor(s_rounds/2+1))}', fg=GREEN)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 



def count_down(count):
    mins = math.floor(count / 60)
    secs = count % 60
    if secs == 0:
        secs = '00'
    elif secs < 10:
        secs = f'0{secs}'
    if mins < 10:
        mins = '0' + str(mins)

    canvas.itemconfig(canvas_text, text=f"{mins}:{secs}")
    if count > 0:
        global timer_set
        timer_set = window.after(1000, count_down, count-1)
    elif count == 0:
        start_clicked()
        marks = ''
        print(1, s_rounds)
        done_check = math.floor(s_rounds / 2)
        print(2, done_check)
        for _ in range(done_check):
            marks += '✔'
        label_check.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)


# Canvas
canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_png = PhotoImage(file='tomato.png')
canvas.create_image(100, 105, image=tomato_png)
canvas_text = canvas.create_text(100, 125, text='00:00', fill='white', font=(FONT_NAME, 25, 'bold'))
canvas.grid(column=1, row=1)

# Label timer
label_timer = Label(text='Timer', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 25, 'bold'))
label_timer.grid(column=1, row=0)
label_timer.config(padx=10, pady=10)

# Label check
label_check = Label(text='', fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, 'bold'))
label_check.grid(column=1, row=3)

# button Start
button_start = Button(text='Start', width=5, command=start_clicked)
button_start.grid(column=0, row=2)

# button Reser
button_reset = Button(text='Reset', width=5, command=time_reset)
button_reset.grid(column=2, row=2)

window.mainloop()