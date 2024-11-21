from tkinter import Tk, Canvas, PhotoImage, Label, Button
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
reps = 0
time_run = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_time():
    window.after_cancel(time_run)
    timer['text']='Timer'
    canvas.itemconfig(time,text='00.00')
    tick['text']=''
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    short_break = SHORT_BREAK_MIN*60
    long_break = LONG_BREAK_MIN*60
    work_min = WORK_MIN*60
    reps+=1
    if reps%8 == 0:
        count_down(long_break)
        timer['text']='Break'
        timer['fg']=RED
    elif reps%2==0:
        count_down(short_break)
        timer['text'] = 'Break'
        timer['fg'] = PINK
    else:
        count_down(work_min)
        timer['text'] = 'Work'
        timer['fg'] = GREEN




# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if count_sec < 10:
        count_sec = f'0{count_sec}'
    canvas.itemconfig(time,text = f'{count_min}:{count_sec}')
    if count>0:
        global time_run
        time_run = window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark+='✔️'
        tick.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100,pady=50,bg=YELLOW)
window.title('Pomodoro')


timer = Label(text='Timer',font=(FONT_NAME,45,'bold'),fg=GREEN,bg=YELLOW)
timer.grid(column = 1,row = 0)

canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_image = PhotoImage(file='tomato.png')
canvas.create_image(100,112,image=tomato_image)
time=canvas.create_text(100,130,text='00.00',fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column = 1,row = 1)

start = Button(text='start',font=(FONT_NAME,10,'bold'),highlightthickness=0,command=start_timer)
start.grid(column = 0,row = 2)

reset = Button(text='reset',font=(FONT_NAME,10,'bold'),highlightthickness=0,command=reset_time)
reset.grid(column = 2,row = 2)

tick = Label(font=(FONT_NAME,10,'bold'),fg=GREEN,bg=YELLOW)
tick.grid(column = 1,row = 3)



window.mainloop()