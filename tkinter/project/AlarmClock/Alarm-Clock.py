# Importing all the necessary libraries to form the alarm clock:
from tkinter import *
import datetime
import time
from playsound import playsound


def alarm(set_alarm_timer):
    try:
        while True:
            time.sleep(1)
            current_time = datetime.datetime.now()

            now = current_time.strftime("%H:%M:%S")
            date = current_time.strftime("%d/%m/%Y")

            print(f"Today: {date}")
            print(now)

            if now == set_alarm_timer:
                print("Time to Wake up")
                playsound("sample.wav")
                break
    except KeyboardInterrupt:
        pass

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)


clock = Tk()
clock.title("DataFlair Alarm Clock")
clock.geometry("400x200")

time_format = Label(clock, text="Enter time in 24 hour format!", fg="red", bg="black", font="Arial").place(x=60, y=150)
addTime = Label(clock, text="Hour  Min   Sec", font=60).place(x=110,y=50)
Label(clock, text="When to wake you up", fg="blue", relief="solid", font=("Helevetica", 7, "bold")).place(x=110)

# The Variables we require to set the alarm(initialization):
hour = StringVar()
min = StringVar()
sec = StringVar()

# Time required to set the alarm clock:
Entry(clock, textvariable=hour, bg="pink", width=15).place(x=110, y=30)
Entry(clock, textvariable=min, bg="pink", width=15).place(x=150, y=30)
Entry(clock, textvariable=sec, bg="pink", width=15).place(x=200, y=30)

# To take the time input by user:
submit = Button(clock, text="Set Alarm", fg="red", width=10,
                command=actual_time).place(x=110, y=70)

clock.mainloop()
# Execution of the window.
