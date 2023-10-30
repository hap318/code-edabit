import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime

def email(): 

    d1 = ukDate(cal1.get_date())
    d2 = ukDate(cal2.get_date())


    today = datetime.today().strftime("%d/%m/%y")
    if d2 == today:
        msg = f"Hi simon,\n\nCould I book off {d1} \n\nThanks,\nHenry"
    else:
        msg = f"Hi simon,\n\nCould I book off {d1} - {d2} \n\nThanks,\nHenry"
    print(msg)

    

def ukDate(date):
    d1 = datetime.strptime(date, "%m/%d/%y")
    ukd1 = d1.strftime("%d/%m/%y")
    return ukd1

root = tk.Tk()
root.geometry("400x500")
root.title("emailer")

cal1 = Calendar(root, selectmode="day")
cal1.pack(pady=20)

cal2 = Calendar(root, selectmode="day")
cal2.pack(pady=20)

submit = tk.Button(root, text="Submit", command=email)
submit.pack()

root.mainloop()