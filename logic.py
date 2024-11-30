import string, random

transitions = []

global start
start = 0

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

        if self.is_start:
            global start
            start = self

    def __str__(self) -> str:
        return f"q{self.num}"

class Automaton:
    def __init__(self, atype:str, states:list) -> None:
        self.atype = atype
        self.states = states

    def add_state(self, state:State):
        self.states.append(state)

def run(word:str):
    if start == 0:
        return "no start found"
    
    spos = []
    for index, t in enumerate(transitions):
        if t["s1"] == start:
            spos.append(t)

    if spos == []:
        return "no transition from start found"
    
    current_state = start

    for index, symbol in enumerate(word):
        state_found = False
        symbol_found = False

        for t in transitions:
            if t["s1"] == current_state:
                state_found = True
                if t["input"] == symbol:
                    print(t["output"])
                    current_state = t["s2"]
                    symbol_found = True
                    break

        if not state_found:
            return f"no transition from state: {current_state} found :("
        elif not symbol_found:
            return f"no transition with symbol: {symbol} at index {index} found :("

    return "success, done"