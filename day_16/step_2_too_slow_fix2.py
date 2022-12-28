
from collections import namedtuple
from copy import deepcopy

filename = "test_input.txt"
#filename = "input.txt"

# data structures (global variables)
caves = {}
Cave = namedtuple("Cave", ["flowrate", "tunnels"])
def add_cave(name, flowrate, tunnels):
    caves[name] = Cave(flowrate, set(tunnels))

with open(filename) as f:
    for line in f:
        # example line: "Valve KZ has flow rate=12; tunnels lead to valves ET, QV, CK, MS"
        line = line.removesuffix("\n")
        line = line.removeprefix("Valve ")
        name, line = line.split(" has flow rate=")
        line = line.replace("s", "") # for: tunnel(s) lead(s) valve(s)
        flowrate_str, line = line.split("; tunnel lead to valve ")
        flowrate = int(flowrate_str)
        tunnels = line.split(", ")
        add_cave(name, flowrate, tunnels)

# more data structures (global variables)
state_original = {
    "my_cave"        : "AA",
    "elephant_cave"  : "AA",
    # little trick, open valves with flowrate zero, so we don't need to check for flowrate zero anymore
    "valves_open"    : {key: False if value.flowrate > 0 else True for key,value in caves.items()},
    "seconds_left"   : 26,
    "total_pressure" : 0,
}

been_here = {}
max_total_pressure = 0
total_skips = 0
total_states = 0
# n_valves_to_open = sum([not open for open in state_original["valves_open"]])

def possible_actions(state, cave):
    possibilities = []
    # we could open the valve in the current cave, if it is closed...
    if not state["valves_open"][cave]:
        possibilities.append('open')
    # ... or we could visit another cave...
    for cave in caves[cave].tunnels:
        possibilities.append(cave)
    return possibilities
    
def apply_action(state, action, who):
    if action == 'open':
        state["valves_open"][state[who]] = True
        state["total_pressure"] += state["seconds_left"] * caves[state[who]].flowrate
    else:
        state[who] = action
    return state

def next_action(state):
    global max_total_pressure, total_skips, total_states

    # print some progress.....
    total_states += 1
    if total_states % 10000 == 0:
        print(total_states, total_skips, len(been_here), max_total_pressure)

    if state["total_pressure"] > max_total_pressure:
        max_total_pressure = state["total_pressure"]

    # have we time left?    
    if state["seconds_left"] == 0:
        return

    # if all valves are open, we don't have to do anything
    if all(state["valves_open"].values()):
        return

    # if we've been in this state with a better result, we can skip this state
    positions = [state["my_cave"], state["elephant_cave"]]
    positions.sort() # inplace
    state_summary = "".join(positions)
    state_summary += "".join(["T" if b else "F" for b in state["valves_open"].values()])
    if state_summary in been_here.keys():
        best_total_pressure, best_seconds_left = been_here[state_summary]
        if best_total_pressure >= state["total_pressure"]:
            if best_seconds_left >= state["seconds_left"]:
                # don't follow this route anymore
                total_skips += 1
                return
    been_here[state_summary] = state["total_pressure"], state["seconds_left"]
    
    # increase time
    state["seconds_left"] -= 1

    actions_for_me = possible_actions(state, state["my_cave"])
    for my_action in actions_for_me:

        #print("my_action", my_action)
        my_state_copy = deepcopy(state)
        my_state_copy = apply_action(my_state_copy, my_action, "my_cave")

        actions_for_elephant = possible_actions(my_state_copy, my_state_copy["elephant_cave"])
        for elephants_action in actions_for_elephant:

            #print("elephants_action :", elephants_action)
            elephants_state_copy = deepcopy(my_state_copy)
            elephants_state_copy = apply_action(elephants_state_copy, elephants_action, "elephant_cave")

            # and continue...
            next_action(elephants_state_copy)

    return # end of: def next_action(state):

next_action(state_original)

print("\n\nresults :\n\n")
print("total_states :", total_states, "\n\n")
print("max_total_pressure :", max_total_pressure, "\n\n")

