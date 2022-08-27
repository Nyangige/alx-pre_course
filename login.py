
from tkinter import *
from tkinter import font
from turtle import bgcolor, title
root=Tk()
#-----defining function-------------
def getvals():
    print("Login successful!")
#-------craeate the size of the window---------
root.geometry("300x200")

#--------background color of the window---------
root.configure(bg="purple")

#----------title of the system----------
root.title("Registration Form")
#------Heading of the form--------
Label(root,text="Registration Form",bg="purple",font="Georgia 15 bold", fg="green").grid(row=0,column=3)
#------form labels-------
name=Label(root,text="Name",fg="black",font="elephant 10 italic",bg="purple")
email=Label(root,text="Email",fg="black",font="elephant 10 italic",bg="purple")
countrycode=Label(root,text="County Code",fg="black",font=" elephant 10 italic",bg="purple")
country=Label(root,text="Country",fg="black",font="elephant 10 italic ",bg="purple")

#make the label fields visible
name.grid(row=1,column=2)
email.grid(row=2,column=2)
countrycode.grid(row=3,column=2)
country.grid(row=4,column=2)

#-------declare the variables-----
namevalue=StringVar
emailvalue=StringVar
countrycodevalue=IntVar
countryvalue=StringVar
checkboxvalue=IntVar

#---------make the entry fields------------
nameentry=Entry(root,textvariable=namevalue,fg="white", borderwidth="3",bg="purple")
emailentry=Entry(root,textvariable=emailvalue, borderwidth="3",bg="purple",fg="white")
countrycodeentry=Entry(root,textvariable=countrycodevalue, borderwidth="3",bg="purple",fg="white")
countryentry=Entry(root,textvariable=countryvalue, borderwidth="3",bg="purple",fg="white")

#-------make the boxes visible----------

nameentry.grid(row=1,column=3)
emailentry.grid(row=2,column=3)
countrycodeentry.grid(row=3,column=3)
countryentry.grid(row=4,column=3)

#------------create a checkbox-------------
Checkbutton(root,text="Remember me?",font="Elephant 10 bold", fg="green",variable=checkboxvalue,bg="purple").grid(row=5,column=3)

#-----------create submit button---------------
Button(text="Submit",font="Elephant 10 bold",fg="green",command=getvals,bg="purple").grid(row=6,column=3)



root.mainloop()