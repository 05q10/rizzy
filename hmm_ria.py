from itertools import product

# Hidden states
states = ["Rainy", "Sunny"]

# Observations
observations = ["walk", "shop", "clean"]

# Initial probabilities
start_prob = {
    "Rainy": 0.6,
    "Sunny": 0.4
}

# Transition probabilities
transition_prob = {
    "Rainy": {"Rainy": 0.7, "Sunny": 0.3},
    "Sunny": {"Rainy": 0.4, "Sunny": 0.6}
}

# Emission probabilities
emission_prob = {
    "Rainy": {
        "walk": 0.1,
        "shop": 0.4,
        "clean": 0.5
    },

    "Sunny": {
        "walk": 0.6,
        "shop": 0.3,
        "clean": 0.1
    }
}

# -----------------------------------
# Generate all possible hidden paths
# -----------------------------------

all_paths = list(product(states, repeat=len(observations)))

max_probability = 0
best_path = None

print("Observation Sequence:")
print(observations)

print("\nAll Path Probabilities:\n")

# -----------------------------------
# Compute probability for each path
# -----------------------------------

for path in all_paths:

    # Start probability
    probability = (
        start_prob[path[0]]
        * emission_prob[path[0]][observations[0]]
    )

    # Remaining transitions + emissions
    for i in range(1, len(path)):

        prev_state = path[i - 1]
        current_state = path[i]

        probability *= (
            transition_prob[prev_state][current_state]
            * emission_prob[current_state][observations[i]]
        )

    # Print path probability
    print(f"{' -> '.join(path)} = {round(probability, 6)}")

    # Track maximum probability
    if probability > max_probability:
        max_probability = probability
        best_path = path

# -----------------------------------
# Display Best Path
# -----------------------------------

print("\nMost Probable Hidden State Path:")
print(" -> ".join(best_path))

print("\nMaximum Probability =", round(max_probability, 6))