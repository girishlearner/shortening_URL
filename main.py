from tkinter import *
import pyshorteners

root = Tk()
root.title("URL Shortener")
root.geometry("600x500")
root.config(bg="#5996F3")
root.resizable(False,False)

def url():
    if url1.get() == '':
        print("Please Enter URL")
    else:
        url_entry = url1.get()
        result = pyshorteners.Shortener().tinyurl.short(url_entry)
        urlE.insert(END, result)

Label(root,text="Generate Short URL",font=("arial",15,"bold"),fg="black",bg="#5996F3").pack(pady=10)

frame = Frame(root)
label = Label(frame,text="URL :",font=("arial",15,"bold"),fg="black",bg="#5996F3").pack(side=LEFT)
url1 = Entry(frame,width=35,font=("arial",15,"bold"),fg="blue")
url1.pack()
frame.pack(pady=10)

Button(root,text="Generate Link",font=("arial",15),fg="red",bg="green",command=url).pack(pady=10)

frame2 = Frame(root)
label1 = Label(frame2,text="Shorted URL : ",font=("arial",15,"bold",),fg="black",bg="#5996F3").pack(side=LEFT)
urlE = Entry(frame2,width=20,font=("arial",15),fg="blue")
urlE.pack()
frame2.pack(pady=10)
root.mainloop()

