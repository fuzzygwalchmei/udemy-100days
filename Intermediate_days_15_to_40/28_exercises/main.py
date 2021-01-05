import tkinter as tk
from tkinter import font
from tkinter.constants import Y
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start():
    countdown(WORK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    minutes, seconds = count//60, count%60
    canvas.itemconfig(timer_text, text = f"{minutes:02}:{seconds:02}")
    if count > 0:
        window.after(1000, countdown, count - 1)


# ---------------------------- UI SETUP ------------------------------- #
 # Create window
window = tk.Tk()
window.config(padx=100, pady=50, bg=YELLOW)
window.title("Pomodoro")


# Create Canvas
canvas = tk.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tk.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

# Create other widgets
lbl_title = tk.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
btn_start = tk.Button(text="Start", bg="white", highlightthickness=0, command=start)
btn_finish = tk.Button(text="Finish", bg="white", highlightthickness=0)
# chk_completed = tk.Checkbutton(bg=YELLOW)
lbl_check = tk.Label(text="✓", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 35, "bold"))

# Put everything on window
lbl_title.grid(row=0, column=1)
canvas.grid(row=1, column=1)
btn_start.grid(row=2, column=0)
btn_finish.grid(row=2, column=2)
lbl_check.grid(row=3, column=1)










window.mainloop()