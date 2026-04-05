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
LONG_BREAK_MIN = 20
reps=0
timer=NONE


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    timer_tex.config(text="Timer")
    tick_mark.config(text="")
    global reps
    reps=0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    print(reps)
    work_sec=WORK_MIN * 60
    short_break_sec=SHORT_BREAK_MIN * 60
    long_break_sec=LONG_BREAK_MIN * 60
    if reps%8==0:
        timer_tex.config(text="Break",fg=RED)
        count_down(long_break_sec)

    elif reps%2==0:
        timer_tex.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        timer_tex.config(text="Work", fg=GREEN)
        count_down(work_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_minute=math.floor(count / 60)
    count_second=count % 60
    # if count_second==0:
    #     count_second="00"
    # for x in range(1,10):
    #     if count_second==x:
    #         count_second=(f"0{x}")
    if count_second<10:
        count_second=f"0{count_second}"
    canvas.itemconfig(timer_text,text=f"{count_minute}:{count_second}")
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        marks = ""
        work_sessions=math.floor(reps/2)
        for _ in range(work_sessions):
            marks+="✔"
            tick_mark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("POMODORO")
window.config(padx=100,pady=50,bg=YELLOW)

canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img)
timer_text=canvas.create_text(103,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
timer_tex=Label(text="TIMER",font=(FONT_NAME,24,"bold"),bg=YELLOW,fg=GREEN)

tick_mark=Label(bg=YELLOW,fg=GREEN,font=(FONT_NAME,19,"bold"))
tick_mark.grid(row=4,column=2)
space=Label(text=" ")
space.grid(row=0,column=0)
timer_tex.grid(row=1,column=2)
start_button=Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=3,column=1)
reset_button=Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=3,column=3)








canvas.grid(row=2,column=2)
window.mainloop()
