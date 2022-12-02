with open("src/day2/input.txt", "r") as f:
    data = [x.strip() for x in f.readlines()]

# Create list of tuples by splitting each line on the space
data = [tuple(x.split(" ")) for x in data]

# Create two lists from the list of tuples, one for the first number, one for the second
opponent_raw = [x[0] for x in data]
suggested_raw = [x[1] for x in data]

choice_map = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "rock",
    "Y": "paper",
    "Z": "scissors",
}

# Create list of opponent plays, and list of suggested plays using the choice_map
opponent = [choice_map[x] for x in opponent_raw]
suggested = [choice_map[x] for x in suggested_raw]


def calc_score(opponent, suggested):
    opponent_wins = []
    suggested_wins = []

    # Loop through the lists of opponent and suggested plays, for each pair, determine who wins
    # losses are zero points, draws are three points, and wins are 6 points
    for i in range(len(opponent)):
        if opponent[i] == suggested[i]:
            opponent_wins.append(3)
            suggested_wins.append(3)
        elif opponent[i] == "rock":
            if suggested[i] == "paper":
                opponent_wins.append(0)
                suggested_wins.append(6)
            elif suggested[i] == "scissors":
                opponent_wins.append(6)
                suggested_wins.append(0)
        elif opponent[i] == "paper":
            if suggested[i] == "rock":
                opponent_wins.append(6)
                suggested_wins.append(0)
            elif suggested[i] == "scissors":
                opponent_wins.append(0)
                suggested_wins.append(6)
        elif opponent[i] == "scissors":
            if suggested[i] == "rock":
                opponent_wins.append(0)
                suggested_wins.append(6)
            elif suggested[i] == "paper":
                opponent_wins.append(6)
                suggested_wins.append(0)

    # Create a score_map where rock, paper, scissors, are worth 1, 2, 3 points respectively
    score_map = {
        "rock": 1,
        "paper": 2,
        "scissors": 3,
    }

    # calculate suggested_play_score and opponent_play_score using the score_map
    suggested_play_score = [score_map[x] for x in suggested]
    opponent_play_score = [score_map[x] for x in opponent]

    # Calculate the total score for each player
    suggested_total_score = sum(suggested_wins) + sum(suggested_play_score)
    opponent_total_score = sum(opponent_wins) + sum(opponent_play_score)

    return (suggested_total_score, opponent_total_score)


print(calc_score(opponent, suggested))

# Part 2

scissors = {"draw": "scissors", "win": "rock", "lose": "paper"}
paper = {"draw": "paper", "win": "scissors", "lose": "rock"}
rock = {"draw": "rock", "win": "paper", "lose": "scissors"}

choice_map_2 = {
    "A": "rock",
    "B": "paper",
    "C": "scissors",
    "X": "lose",
    "Y": "draw",
    "Z": "win",
}

strat_map = {
    "rock": rock,
    "paper": paper,
    "scissors": scissors,
}
opponent = [choice_map_2[x] for x in opponent_raw]
suggested = [choice_map_2[x] for x in suggested_raw]

suggested_plays = []
for o, s in zip(opponent, suggested):
    if s == "lose":
        suggested_plays.append(strat_map[o]["lose"])
    elif s == "draw":
        suggested_plays.append(strat_map[o]["draw"])
    elif s == "win":
        suggested_plays.append(strat_map[o]["win"])

print(calc_score(opponent, suggested_plays))
