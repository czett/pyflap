from tkinter import *
import logic as lg
import vis

state_dict = {}
states = []
transitions = []

# Methods
def create():
    try:
        if states == []:
            start_state = True
        else:
            start_state = False
            
        sname = name.get()
        created_state = lg.State(start_state, False, sname)
        states.append(created_state)
        state_dict[f"{sname}"] = created_state

        print(states)
        print(transitions)
    except:
        error_msg.config(text="Damn there was some error while crearing your state, arghhh!")

def connect():
    try:
        s1 = s1_name.get()
        s2 = s2_name.get()
        i = input_symbol.get()
        o = output.get()

        lg.connect(state_dict[s1], state_dict[s2], i, o)
        t = (f"q{s1}", f"q{s2}", f"{i} / {o}")
        transitions.append(t)

        print(states)
        print(transitions)
    except:
        error_msg.config(text="Damn there was some error while connecting the states :(")

def run():
    try:
        word = word_name.get()
        print(lg.run(word))
        vis.graph(states, transitions)
    except:
        error_msg.config(text="Damn there was some error while running the automaton!")


root = Tk()
root.title("PyFlap")
root.geometry("800x600")

# base labels
title = Label(text="PyFlap")
title["font"] = "Arial 20 bold"
title.pack(pady=10)

error_msg = Label(text="", fg="#ff0000")
error_msg["font"] = "Arial 14 bold"
error_msg.pack(pady=0)

subtitle = Label(text="Create automata here!\n------------------------------")
subtitle["font"] = "Arial 14 bold"
subtitle.pack(pady=0)

# create form
create_label = Label(text="Create a new state:")
create_label["font"] = "Arial 14"
create_label.pack(pady=0)

name = Entry(root)
name.insert(0, "number")
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