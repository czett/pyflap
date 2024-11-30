# PyFlap

**PyFlap** is a lightweight Python-based tool inspired by JFLAP, designed for working with automata in theoretical computer science. It provides functionality to define states, transitions, run input words through the automaton, and visualize the automaton with a graphical user interface (GUI).

## Features

- Define states and transitions for automata.
- Handle inputs and track state changes.
- Supports customizable input (`σ`) and output (`γ`) alphabets.
- Visualize automata using NetworkX and Matplotlib.
- Graphical user interface (GUI) to create states, define transitions, and run the automaton.

## Example

Here's an example of an automaton:

- Three states: start (`q0`), end (`q2`), broken (`q1`).
- Transitions for turning a switch ON/OFF and breaking it.

```python
start = State(True, False, 0)
broken = State(False, False, 1)
end = State(False, True, 2)

connect(start, end, "D", "ON")  # Turn switch on
connect(end, start, "D", "OFF")  # Turn switch off
connect(end, broken, "S", "BROKEN")  # Break switch

print(run("DDDSD"))
```

### Visualizing the Automaton

PyFlap can plot automata using `NetworkX` and `Matplotlib`. For the above example, the visualization would include:

- **States** (`q0`, `q1`, `q2`) represented as nodes.
- **Transitions** (`D / ON`, `D / OFF`, `S / BROKEN`) as labeled edges.
- Curved arrows for readability in cases of overlapping transitions.

## GUI for Creating Automata

With PyFlap's GUI, users can:

- **Create states** by entering a state name and selecting if it's the start state.
- **Define transitions** between states, including the input symbol and output label.
- **Run the automaton** with a user-provided word to check its behavior.

### Error Handling (Currently Missing)

At the moment, **PyFlap** lacks proper error handling for several aspects of automaton creation and simulation. Here's what needs to be addressed:

1. **State Creation**:
   - **Validation**: Ensure state names are unique and properly formatted.
   - **Start State**: Allow only one state to be marked as the start state.
   
2. **Transition Definition**:
   - **State Existence**: Ensure that both source and destination states exist before attempting to define a transition.
   - **Input/Output Validation**: Check that input symbols and outputs are valid and meet the automaton's alphabet constraints.
   
3. **Run Simulation**:
   - **Invalid States**: Handle cases where the word contains symbols that lead to undefined or unreachable states.
   - **Edge Case Handling**: Properly manage edge cases, such as empty transitions or cyclic automata without end states.
   
4. **GUI Errors**:
   - **Empty Fields**: Ensure all input fields (state names, symbols, etc.) are not empty before allowing actions.
   - **Invalid Inputs**: Alert the user when input symbols, state names, or transitions are not valid.

These improvements are essential to ensure that the application runs smoothly and guides users through the automaton creation and simulation process without unexpected failures.

### License

This project is released under the MIT License.
