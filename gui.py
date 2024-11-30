# just for testing, no functionality, run app.py

from tkinter import *

def create():
    print("")
def connect():
    print("")
def run():
    print("")

root = Tk()
root.title("PyFlap")
root.geometry("800x600")

# base labels
title = Label(text="PyFlap")
title["font"] = "Arial 20 bold"
title.pack(pady=10)

subtitle = Label(text="Create automata here!\n------------------------------")
subtitle["font"] = "Arial 14 bold"
subtitle.pack(pady=0)

# create form
create_label = Label(text="Create a new state:")
create_label["font"] = "Arial 14"
create_label.pack(pady=0)

name = Entry(root)
name.insert(0, "q0")
name.pack()

create_btn = Button(root, text="Create", command=create)
create_btn.pack(pady=10)

# connect form
create_label = Label(text="Create a transition:")
create_label["font"] = "Arial 14"
create_label.pack(pady=0)

s1_name = Entry(root)
s1_name.insert(0, "start state (eg q0)")
s1_name.pack()

s2_name = Entry(root)
s2_name.insert(0, "end state (eg q1)")
s2_name.pack()

input_symbol = Entry(root)
input_symbol.insert(0, "input for tr.")
input_symbol.pack()

output = Entry(root)
output.insert(0, "output")
output.pack()

connect_btn = Button(root, text="Connect", command=connect)
connect_btn.pack(pady=10)

# create form
run_label = Label(text="Run with word:")
run_label["font"] = "Arial 14"
run_label.pack(pady=0)

word_name = Entry(root)
word_name.insert(0, "word of symbols")
word_name.pack()

run_btn = Button(root, text="Run and render", command=run)
run_btn.pack(pady=10)

root.mainloop()