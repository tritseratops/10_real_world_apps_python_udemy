from tkinter import Entry, Button, Text, StringVar, Tk, END, Label


window = Tk()

def kg_to_gramms(weight):
    return weight*1000

def kg_to_pounds(weight):
    return weight*2.20462

def kg_to_ounces(weight):
    return weight*35.274

def convert():
    gramms = kg_to_gramms(float(kg_value.get()))
    pounds = kg_to_pounds(float(kg_value.get()))
    ounces =kg_to_ounces( float(kg_value.get()))
    gramms_value.set(gramms)
    pounds_value.set(pounds)
    ounces_value.set(ounces)

# set controls
l_kg = Label(window, text="Kg:")
l_kg.grid(row=0,column=0, rowspan=2)

kg_value = StringVar()
kg = Entry(window, textvariable=kg_value)
kg.grid(row=0, column=2, rowspan=2)

b1 = Button(window, text="Convert", command=convert)
b1.grid(row=0, column=4, rowspan=2)


l_gramms = Label(window, text="Gramms:")
l_gramms.grid(row=2,column=0)

gramms_value=StringVar()
res_gramms = Label(window, textvariable=gramms_value, text="")
res_gramms.grid(row=2,column=1)

l_pounds = Label(window, text="Pounds:")
l_pounds.grid(row=2,column=2)

pounds_value=StringVar()
res_pounds = Label(window, textvariable=pounds_value, text="")
res_pounds.grid(row=2,column=3)

l_ounces = Label(window, text="Ounces:")
l_ounces.grid(row=2,column=4)

ounces_value=StringVar()
res_ounces = Label(window, textvariable=ounces_value, text="")
res_ounces.grid(row=2,column=5)


window.mainloop()

