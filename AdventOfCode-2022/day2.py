from input_day2 import strategy

# elf
# rock = "A",  paper = "B", scissors = "C"

# me
# rock = "X" , paper = "Y", scissors = "Z"

win = [{"A":"Y"}, {"B":"Z"}, {"C":"X"}]
draw = [{"A":"X"}, {"B":"Y"}, {"C":"Z"}]
lose = [{"A":"Z"}, {"B":"X"}, {"C":"Y"}]

# score shape
score_X = 1
score_Y = 2
score_Z = 3

# score round
score_win = 6
score_tie = 3
score_lost = 0

total_score = []

for x, y in strategy.items():
  if {x, y} == win[0]:
    total_score.append(score_Y + score_win)
  elif {x, y} == win[1]:
    total_score.append(score_Z + score_win)
  elif {x, y} == win[2]:
    total_score.append(score_X + score_win)
  elif {x, y} == draw[0]:
    total_score.append(score_X + score_tie)
  elif {x, y} == draw[1]:
    total_score.append(score_Y + score_tie)
  elif {x, y} == draw[2]:
    total_score.append(score_Z + score_tie)
  elif {x, y} == lose[0]:
    total_score.append(score_Z + score_lost)
  elif {x, y} == lose[1]:
    total_score.append(score_X + score_lost)
  elif {x, y} == lose[2]:
    total_score.append(score_Y + score_lost)
print(sum(total_score))




#part 2

# "X" = lose
# "Y" = tie
# "Z" = win

# for x in range (0, len(strategy)):
#   print x[1]



