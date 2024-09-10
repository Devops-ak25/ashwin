from tkinter import *
from tkinter import messagebox

def validate_input(name, email, password,confirm_password,phone_no):
    if not name or not email or not password or not confirm_password or not phone_no:
        return "All fields should be filled"
    if "@" not in email or ".com" not in email:
        return "Email should contain @ and ."
    if len(password)<8:
        return "Enter valid password"
    if password != confirm_password:
        return "ReEnter the password"
    if not phone_no.isdigit():
        return "Enter only digits"
    if len(phone_no) != 10:
        return "Phone number must be 10 digits"
        
def submit_form():
    name = name_entry.get()
    email=email_entry.get()
    password = password_entry.get()
    confirm_password = confirm_password_entry.get()
    phone_no = mobile_entry.get()
    
    error = validate_input(name,email,password,confirm_password,phone_no)
    if error:
        messagebox.showerror("Error", error)
    else:
        messagebox.showinfo("Success","Registration Successfull")
        
root=Tk()
root.title("Registration Form")

Label(root,text="Name:").grid(row=0, column=0,padx=5,pady=10)
Label(root, text="Email:").grid(row=1, column=0, padx=5, pady= 10)
Label(root, text="Password:").grid(row=2, column=0, padx=5, pady= 10)
Label(root, text="Confirm Password:").grid(row=3, column=0, padx=5, pady= 10)
Label(root, text="Mobile No.:").grid(row=4, column=0, padx=5, pady= 10)


name_entry=Entry(root)
email_entry = Entry(root)
password_entry = Entry(root,show="*")
confirm_password_entry = Entry(root,show="*")
mobile_entry = Entry(root)

name_entry.grid(row=0,column=1,padx=5,pady=10)
email_entry.grid(row=1,column=1,padx=5,pady=10)
password_entry.grid(row=2,column=1,padx=5,pady=10)
confirm_password_entry.grid(row=3,column=1,padx=5,pady=10)
mobile_entry.grid(row=4,column=1,padx=5,pady=10)

submit_button = Button(text="submit",command=submit_form)
submit_button.grid(row=6,column=1,padx=5,pady=10)

root.mainloop()