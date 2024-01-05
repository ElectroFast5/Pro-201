from tkinter import *

window=Tk()
window.title("Interest Calculator")
window.geometry("380x400")
window.configure(bg="gray")

def calculateBMI():
    interest=round((float(principleEntry.get())*float(rateEntry.get())*float(timeEntry.get()))/100,2)
    resultLabel.destroy()
    outputMessage=Label(resultFrame,text=f"Your interest is £{interest}",bg="gray",font=("Calibri",12),width=42)
    outputMessage.place(x=20,y=40)
    outputMessage.pack()

appLabel=Label(window,text="Interest Calculator",fg="black",bg="gray",font=("Calabri",20),bd=5)
appLabel.place(x=50,y=20)

principleLabel=Label(window,text="Enter principle: ",fg="black",bg="gray",font=("Calibri",12),bd=1)
principleLabel.place(x=20,y=90)

principleEntry=Entry(window,text="",bd=2,width=22)
principleEntry.place(x=150,y=92)

rateLabel=Label(window,text="Enter rate: ",fg="black",bg="gray",font=("Calibri",12),bd=1)
rateLabel.place(x=20,y=140)

rateEntry=Entry(window,text="",bd=2,width=22)
rateEntry.place(x=150,y=142)

timeLabel=Label(window,text="Enter time: ",fg="black",bg="gray",font=("Calibri",12),bd=1)
timeLabel.place(x=20,y=185)

timeEntry=Entry(window,text="",bd=2,width=22)
timeEntry.place(x=150,y=187)

button=Button(window,text="Calculate",bg="purple",bd=4,fg="black",command=calculateBMI)
button.place(x=20,y=250)

resultFrame=LabelFrame(window,text="result",bg="gray",font=("Calibri",12))
resultFrame.pack(padx=20,pady=20)
resultFrame.place(x=20,y=300)

resultLabel=Label(resultFrame,text="",bg="gray",font=("Calibri",12),width=33)
resultLabel.place(x=20,y=20)
resultLabel.pack()

window.mainloop()