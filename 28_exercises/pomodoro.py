import tkinter as tk
from tkinter import Image, font
from tkinter.constants import Y
from PIL import ImageTk

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None
running = False

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global running
    window.after_cancel(timer)
    canvas.itemconfig(txt_timer, text = "00:00")
    lbl_title.config(text = "Timer", fg=GREEN)
    lbl_check.config(text="")
    running = False


# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    global running
    if running == True:
        return
    elif reps%8 == 0:
        timer_time, timer_text, colour = LONG_BREAK_MIN, "Break", RED
    elif reps%2 == 0:
        timer_time, timer_text, colour  = SHORT_BREAK_MIN, "Break", PINK
    else:
        timer_time, timer_text, colour  = WORK_MIN, "Work", GREEN

    lbl_title.config(text=timer_text, fg=colour)
    running = True
    countdown(timer_time * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    global reps
    global timer
    minutes, seconds = int(count//60), int(count%60)
    canvas.itemconfig(txt_timer, text = f"{minutes:02}:{seconds:02}")
    if count > 0:
        timer = window.after(1000, countdown, count - 1)
    else:
        reps += 1
        start_timer()
        lbl_check.config(text = f"{(reps//2)%4 * '✓'}")


# ---------------------------- UI SETUP ------------------------------- #
 # Create window
window = tk.Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")


# Create Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = ImageTk.PhotoImage(file="tomato.png")
# tomato_img.show()
canvas.create_image(100, 112, image=tomato_img)
txt_timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Create other widgets
lbl_title = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
btn_start = tk.Button(text="Start", bg="white", highlightthickness=0, command=start_timer)
btn_finish = tk.Button(text="Finish", bg="white", highlightthickness=0, command=reset_timer)
# chk_completed = tk.Checkbutton(bg=YELLOW)
lbl_check = tk.Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))

# Put everything on window
lbl_title.grid(row=0, column=1)
canvas.grid(row=1, column=1)
btn_start.grid(row=2, column=0)
btn_finish.grid(row=2, column=2)
lbl_check.grid(row=3, column=1)










window.mainloop()