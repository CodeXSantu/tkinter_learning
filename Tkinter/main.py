from tkinter import*

window = Tk()
window.title("First tkinter program")
window.minsize(width=500,height=500)

#!---------------------Label------------------------------
my_label = Label(text="I am  Label", font=("Arial",40,"bold"), )
my_label.pack()

my_label["text"] = "new text"


#! ------------------------BUTTON ----------------------------

def button_clicked():
    print("i got clicked")
    my_label.config(text=f"{input.get()}")
    button.config(text="Submited")

button = Button(text ="Submit",font=("Arial",10,"normal"),command=button_clicked)
button.pack()

#! ------------------------ENTRY-------------------------------------------
input = Entry(width= 30)
input.pack()


#!-------------------------TEXT----------------------------------------------
text = Text(width=30,height=5)
#?put cursor in the text box
text.focus()
#?adds some text to begin with
text.insert(END, "Example of mutline texr entry.")
#?get current value in textboc at lin 1,character 0
print(text.get("1.0",END))
text.pack()

#!------------- Spinbox----------------------------
def spinbox_used():
    #?gets the corrent value in spinbox
    print(spinbox.get())
spinbox = Spinbox(fr = 0, to=10,width =5, command = spinbox_used)
spinbox.pack()
#! -------------------------SCALE-------------------------------------
def scale_used(value):
    print(value)
    
scale = Scale(fr=0,to=100,command = scale_used)
scale.pack()

#! -----------------------------CHECKBUTTON-----------------------
def checkbutton_used():
    #?print 1 ig on  button checked.otherwise 0.)
    print(checked_state.get())
#?variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="is on ?",variable = checked_state, command = checkbutton_used)
checked_state.get()
checkbutton.pack()

#!----------------------------Radiobutton-------------------------------
def radio_used():
    print(radio_state.get())
#?ariable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


#!------------------------------Listbox-------------------------------------
def listbox_used(event):
    #?Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()





window.mainloop()