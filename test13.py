# my_bag = "Crossover", "Shamgod", "Btbwrap", "Spinmove"
# for steps in my_bag:
#     print(steps)

# data = []

# mybag = ["Crossover", "Shamgod", "Btbwrap", "Spinmove"]

# for m in range(1, 5):
#     data.append([m, mybag[m-1]])

# for sublist in mybag:
#     print(*sublist)

# for y in range(7,11):
#     print("Number",y)

data = []

my_bag = ["Crossover", "Shamgod", "Btbwrap", "Spinmove"]

for i in range(1, 5):
    data.append([i, my_bag[i-1]])

for sublist in data:
    print(*sublist)