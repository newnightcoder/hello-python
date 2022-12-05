from input_day1 import elves

#print(len(elves))
# print(sum(elves[0]))

#part 1
list = []
for elf in elves:
  list.append(sum(elf))
print(max(list))

#part 2
list.sort(reverse=True) 
top3 = []
for x in range(0, 3):
  top3.append(list[x])
print(sum(top3))


