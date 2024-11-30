# PyFlap

**PyFlap** is a lightweight Python-based tool inspired by JFLAP, designed for working with automata in theoretical computer science. It provides basic functionality to define states, transitions, and run input words through the automaton.

## Features

- Define states and transitions for automata.
- Handle inputs and track state changes.
- Supports customizable input (`σ`) and output (`γ`) alphabets.
- Includes a sample automaton for demonstration.
- Visualize automata using NetworkX and Matplotlib.

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

### Visualizing the Automaton

PyFlap can plot automata using `NetworkX` and `Matplotlib`. For the above example, the visualization would include:

- **States** (`q0`, `q1`, `q2`) represented as nodes.
- **Transitions** (`D / ON`, `D / OFF`, `S / BROKEN`) as labeled edges.
- Curved arrows for readability in cases of overlapping transitions.

## Output

The script will:
- Print outputs of transitions.
- Notify if the automaton encounters invalid inputs or unreachable states.
- Display a clear graphical representation of the automaton if visualization is enabled.

### License

This project is released under the MIT License.
