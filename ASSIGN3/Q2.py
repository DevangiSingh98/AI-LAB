# matrix: percepts + rules + actions
rule_matrix = [
    # in  out  obs  emg   gate   siren  signal
    [0,   0,   0,   1,   "lower", "on",  "red"],    # Manual emergency
    [1,   0,   1,   0,   "lower", "on",  "red"],    # Train + obstacle
    [0,   1,   1,   0,   "lower", "on",  "red"],    # Train + obstacle
    [1,   0,   0,   0,   "lower", "on",  "green"],  # Inbound train
    [0,   1,   0,   0,   "lower", "on",  "green"],  # Outbound train
    [0,   0,   0,   0,   "raise", "off", "green"]   # Normal operation
]

def agent(percept):
    inbound, outbound, obstacle, emergency = percept

    for rule in rule_matrix:
        rin, rout, robs, remg, gate, siren, signal = rule

        if (inbound == rin and
            outbound == rout and
            obstacle == robs and
            emergency == remg):
            return (gate, siren, signal)

percepts = [
    (0,0,0,0),              # Not detected
    (1,0,0,0),              # Inbound train
    (1,0,1,0),              # Train + obstacle
    (0,0,0,1),              # Manual Emergency
    (0,0,0,0)               # Not detected
]

step = 1

for p in percepts:
    action = agent(p)
    print("Step-", step)
    print("Percept (in, out, obs, emg):", p)
    print("Action (gate, siren, signal):", action, "\n")
    step += 1
