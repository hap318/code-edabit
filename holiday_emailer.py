import tkinter as tk
from tkcalendar import Calendar
from datetime import datetime
from email.message import EmailMessage
import ssl
import smtplib

def email(): 

    d1 = ukDate(cal1.get_date())
    d2 = ukDate(cal2.get_date())


    today = datetime.today().strftime("%d/%m/%y")
    if d2 == today:
        msg = f"Hi simon,\n\nCould I book off {d1} \n\nThanks,\nHenry"
    else:
        msg = f"Hi simon,\n\nCould I book off {d1} - {d2} \n\nThanks,\nHenry"

    f = open(r"C:\Users\henry\Desktop\Files\emailer.txt", "r")
    host_email = f.readline().strip()
    password = f.readline().strip()
    app_pass = f.readline().strip()

    email_reciever = "h4p2001@gmail.com"
    subject = "holiday request"


    em = EmailMessage()
    em["From"] = host_email
    em["To"] = email_reciever
    em["Subject"] = subject
    em.set_content(msg)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
        smtp.login(host_email, app_pass)
        smtp.sendmail(host_email, email_reciever, em.as_string())
        print("Email sent!")
        print("Email preview: ", msg)
    

    

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