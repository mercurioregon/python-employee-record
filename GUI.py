rom tkinter import  *

root = Tk()
root.title("Welcome to my Visual Display")
root.geometry('350x200')

lbl = Label(root, text = "Your name is Jim, right?")
lbl.grid()

txt = Entry(root, width=10)
txt.grid(column =1, row=0)

#INCLUDES BUTTON RESPONSE AND TEXT FIELD
def clicked():
    res = "You wrote:" + txt.get()
    # lbl.configure(text = "I was just, like, clicked and stuff.")
    lbl.configure(text = res)
btn = Button(root, text = "Click me, man." ,
                           fg = "red",  command =clicked)
btn.grid(column=2, row=0)

root.mainloop()