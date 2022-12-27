
from collections import namedtuple
from copy import deepcopy

#filename = "test_input.txt"
filename = "input.txt"

# data structures (global variables)
caves = {}
Cave = namedtuple("Cave", ["flowrate", "tunnels"])
def add_cave(name, flowrate, tunnels):
    caves[name] = Cave(flowrate, set(tunnels))

with open(filename) as f:
    for line in f:
        line = line.removesuffix("\n")
        line = line.removeprefix("Valve ")
        name, line = line.split(" has flow rate=")
        line = line.replace("s", "") # for: tunnel(s) lead(s) valve(s)
        flowrate_str, line = line.split("; tunnel lead to valve ")
        flowrate = int(flowrate_str)
        tunnels = line.split(", ")
        add_cave(name, flowrate, tunnels)

# print(caves)

# more data structures (global variables)
state_original = {
    "current_cave"   : "AA",
    "valves_open"    : {key: False for key in caves.keys()},
    "seconds_left"   : 30,
    "actions"        : [],  # can be cave name for a move, 'open' or 'none'
    "total_pressure" : 0,
}

been_here = {}
max_total_pressure = 0
max_actions = []
total_skips = 0
total_states = 0

def next_action(state):
    global max_total_pressure, max_actions, total_skips, total_states

    # print some progress.....
    total_states += 1
    if total_states % 1000000 == 0:
        print(total_states, total_skips, len(been_here), max_total_pressure)
        print(state["actions"])

    if state["total_pressure"] > max_total_pressure:
        max_total_pressure = state["total_pressure"]
        max_actions = state['actions']

    # have we been here before at this time with a better total pressure
    summary = state["current_cave"] + "".join(["T" if b else "F" for b in state["valves_open"].values()])
    if summary in been_here.keys():
        best_total_pressure, best_seconds_left = been_here[summary]
        if best_total_pressure >= state["total_pressure"]:
            if best_seconds_left >= state["seconds_left"]:
                # don't follow this route anymore
                total_skips += 1
                return
    been_here[summary] = state["total_pressure"], state["seconds_left"]
    
    # have we time left?    
    if state["seconds_left"] == 0:
        return

    # increase time
    state["seconds_left"] -= 1
    
    # if all valves are open, we don't have to do anything
    if all(state["valves_open"].values()):
        state_copy = deepcopy(state) 
        state_copy["actions"].append('none')
        next_action(state_copy)
        return

    # we could open the valve in the current cave, if it is closed...
    # (only useful if the flowrate is unequal zero)
    if (    (not state["valves_open"][state["current_cave"]])
        and caves[state["current_cave"]].flowrate != 0):
        
        state_copy = deepcopy(state) 
        state_copy["valves_open"][state["current_cave"]] = True
        # we now can calculate the total pressure released by this valve
        state_copy["total_pressure"] += state["seconds_left"] * caves[state["current_cave"]].flowrate
        state_copy["actions"].append('open')
        # and continue...
        next_action(state_copy)

    # ... or we could visit another cave...
    for cave in caves[state["current_cave"]].tunnels:
        state_copy = deepcopy(state) 
        state_copy["current_cave"] = cave
        state_copy["actions"].append(cave)
        # and continue...
        next_action(state_copy)

    return        

next_action(state_original)

print("\n\nresults :\n\n")
print("total_states :", total_states, "\n\n")
print("max_actions :", max_actions, "\n\n")
print("max_total_pressure :", max_total_pressure, "\n\n")

