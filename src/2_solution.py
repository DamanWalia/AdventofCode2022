FILEPATH = "./input/2_input.txt"

# solution for part 1
def score(play):
    """
    rock < paper < scissor < rock 
    A and X rock = 1
    B and Y paper = 2
    C and Z scissor = 3
    win = 6, lose = 0, draw = 3
    """
    judge = {"AY":8, "BZ":9, "CX":7, # win + choice
             "AX":4, "BY":5, "CZ":6, # draw + choice
             "AZ":3, "BX":1, "CY":2} # lose + choice
    return judge[play]

with open(FILEPATH) as input:
    total_score = 0
    for play in input:
        total_score += score(play.strip().replace(" ", ""))
print(total_score)

# solution for part 2
def score(play):
    """
    rock < paper < scissor < rock 
    X means lose
    Y means draw
    Z means win
    win = 6, lose = 0, draw = 3
    """
    score = 0
    point = {"A":1, "B":2, "C":3}
    win = {"A":"B", "B":"C", "C":"A"}
    lose = {"A":"C", "B":"A", "C":"B"}
    if play[1] == "X":
        score = point[lose[play[0]]]
    elif play[1] == "Y":
        score = 3 + point[play[0]]
    elif play[1] == "Z":
        score = 6 + point[win[play[0]]]
    return score

with open(FILEPATH) as input:
    total_score = 0
    for play in input:
        total_score += score(play.strip().replace(" ", ""))
print(total_score)