from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox

window = Tk()
window.title("Registration Form")
window.geometry("600x400")

l1 = Label(window, text="REGISTRATION FORM", font=("Arial", 20))
l1.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
l2 = Label(window, text="Full Name:", font=("Arial", 16))
l2.grid(row=1, column=0, padx=5, pady=5, sticky=E)
l3 = Label(window, text="Email ID:", font=("Arial", 16))
l3.grid(row=2, column=0, padx=5, pady=5, sticky=E)
l4 = Label(window, text="Gender:", font=("Arial", 16))
l4.grid(row=3, column=0, padx=5, pady=5, sticky=E)
l5 = Label(window, text="Country:", font=("Arial", 16))
l5.grid(row=5, column=0, padx=5, pady=5, sticky=E)
l6 = Label(window, text="Programming:", font=("Arial", 16))
l6.grid(row=6, column=0, padx=5, pady=5, sticky=E)

name = StringVar()
mail = StringVar()
e1 = Entry(window, textvariable=name, font=("Arial", 16))
e1.grid(row=1, column=1, padx=5, pady=5)
e2 = Entry(window, textvariable=mail, font=("Arial", 16))
e2.grid(row=2, column=1, padx=5, pady=5)

Gender = StringVar()
r1 = Radiobutton(window, text="Male", variable=Gender, value="Male", font=("Arial", 12))
r1.grid(row=3, column=1, sticky=W)
r2 = Radiobutton(window, text="Female", variable=Gender, value="Female", font=("Arial", 12))
r2.grid(row=4, column=1, sticky=W)

Country = StringVar()
C1 = Combobox(window, textvariable=Country, values=["INDIA", "USA", "UK", "GERMANY", "OTHER"], font=("Arial", 12))
C1.grid(row=5, column=1, padx=5, pady=5)

Java = StringVar(value="NO")
Python = StringVar(value="NO")
c1 = Checkbutton(window, text="Java", variable=Java, onvalue="YES", offvalue="NO", font=("Arial", 12))
c1.grid(row=6, column=1, sticky=W)
c2 = Checkbutton(window, text="Python", variable=Python, onvalue="YES", offvalue="NO", font=("Arial", 12))
c2.grid(row=7, column=1, sticky=W)

def submit():
    info = f"Full Name: {name.get()}\n"
    info += f"Email ID: {mail.get()}\n"
    info += f"Gender: {Gender.get()}\n"
    info += f"Country: {Country.get()}\n"
    
    programming_languages = []
    if Java.get() == "YES":
        programming_languages.append("Java")
    if Python.get() == "YES":
        programming_languages.append("Python")
    
    if programming_languages:
        info += "Known Programming Languages: " + ", ".join(programming_languages) + "\n"
    else:
        info += "Known Programming Languages: None\n"
    
    message = f"Hi {name.get()},\n\nClick Yes if the below details are correct \n\n{info}"
    response = messagebox.askyesno("Confirmation Box", message)
    if response:
        with open("registration_details.txt", "a") as file:
            file.write(info + "\n\n")
        messagebox.showinfo("Success", "Details stored successfully")
        window.destroy()

b1 = Button(window, text="SUBMIT", command=submit, font=("Arial", 14), fg="White", bg="Red")
b1.grid(row=8, column=0, padx=5, pady=5, columnspan=2)

window.mainloop()
