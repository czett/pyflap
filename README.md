# PyFlap

**PyFlap** is a lightweight Python-based tool inspired by JFLAP, designed for working with automata in theoretical computer science. It provides basic functionality to define states, transitions, and run input words through the automaton.

## Features

- Define states and transitions for automata.
- Handle inputs and track state changes.
- Supports customizable input (`σ`) and output (`γ`) alphabets.
- Includes a sample automaton for demonstration.

## Example

Here's an example of an automaton:

- Three states: start (`q0`), end (`q2`), broken (`q1`).
- Transitions for turning a switch ON/OFF and breaking it.

```python
start = State(True, False, 0)
broken = State(False, False, 1)
end = State(False, True, 2)

connect(start, end, "D", "ON") # turn switch on
connect(end, start, "D", "OFF") # turn switch off
connect(end, broken, "S", "BROKEN") # break switch

print(run("DDDSD"))
```

## Output

The script will print outputs of transitions and notify if the automaton encounters invalid inputs or unreachable states.

### License

This project is released under the MIT License.
