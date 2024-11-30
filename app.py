import logic as lg

start = lg.State(True, False, 0)
broken = lg.State(False, False, 1)
end = lg.State(False, True, 2)

lg.connect(start, end, "D", "ON") # turn switch on
lg.connect(end, start, "D", "OFF") # turn switch off
lg.connect(end, broken, "S", "BROKEN") # break switch, maybe destroying it for context, only possible when turned on

print(lg.run("DDDSD"))