from tkinter import Entry, Button, Text, StringVar, Tk, END


window = Tk()

def km_to_miles():
    # print(e_value.get())
    miles = float(e_value.get())/1.6
    t1.insert(END,miles)
    return e_value.get()
b1 = Button(window, text="Execute", command=km_to_miles)
# b1.pack()

b1.grid(row=0, column=0, rowspan=1)

e_value = StringVar()
e1 = Entry(window, textvariable=e_value)
e1.grid(row=1, column=0)


t1 = Text(window, height=1, width=20)

t1.grid(row=0, column=1)
window.mainloop()

