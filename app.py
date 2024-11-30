import logic as lg
import vis

# nodes/states
start = lg.State(True, False, 0)
broken = lg.State(False, False, 1)
end = lg.State(False, True, 2)

lg.connect(start, end, "D", "ON")  # Turn switch on
lg.connect(end, start, "D", "OFF")  # Turn switch off
lg.connect(end, broken, "S", "BROKEN")  # Break switch

print(lg.run("DDDS"))

# plotting
states = ["q0", "q1", "q2"]
transitions = [
    ("q0", "q2", "D / ON"),
    ("q2", "q0", "D / OFF"),
    ("q2", "q1", "S / BROKEN"),
]
vis.graph(states, transitions)