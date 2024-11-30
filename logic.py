import string, random

transitions = []

# tuple notation
sigma = []
gamma = []
q = []

def get_id(length:int):
    return "".join([random.choice(string.ascii_lowercase) for i in range(length)])

def connect(s1, s2, inp, out):
    transition = {"_id": get_id(16), "s1": s1, "s2": s2, "input": inp, "output": out}
    transitions.append(transition)

    if inp not in sigma:
        sigma.append(inp)
    
    if out not in gamma:
        gamma.append(out)

class State:
    def __init__(self, is_start:bool, is_end:bool, num:int) -> None:
        self.is_end = is_end
        self.is_start = is_start
        self.num = num
        
        q.append(self)

class Automaton:
    def __init__(self, atype:str, states:list) -> None:
        self.atype = atype
        self.states = states

    def add_state(self, state:State):
        self.states.append(state)

start = State(True, False, 0)
end = State(False, True, 1)

connect(start, end, "D", "AN")
connect(end, start, "D", "AUS")

def run(word:str):
    for t in transitions:
        if t["s1"] == start:
            print("start found")

run("")