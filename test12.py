# height = float(input("Enter height : "))
# if height >= 5.8:
#     print("You are tall")
# else:
#     print("You are short")

# answer = input("""Type 1 for 10_Robux,
# Type 2 for 20_Robux,
# Type 3 for 30_Robux,
# """)
# if answer == "1":
#     print("You have purchased 10_Robux")
# elif answer =="2":
#     print("You have purchased 20_Robux")
# elif answer =="3":
#     print("You have purchased 30_Robux")
# else:
#     print("You can only type 1, 2, 3")

# height_feet = int(input("Enter your height in feet : "))
# height_inches = int(input("Enter your height inches : "))
# if height_feet >=5 and height_inches >=7:
#     print("You are tall")
# else:
#     print("You are short")

# answer = 7
# guess = int(input("Enter your guess (1 - 10) : "))
# if guess > answer:
#     print("Wrong guess. Try smaller one ")
# elif guess < answer:
#     print("Wrong guess. Try bigger one ")
# elif guess == answer:
#     print("Bingo!")

# answer = input("Enter Weather (sunny, rainy, windy)")
# if answer == "sunny":
#     print("It's sunny let's go ball")
# elif answer == "windy":
#     print("It's windy, let just chill")
# elif answer == "rainy":
#     print("It's rainyy, let's go balllll!!!!!!!!!")

import random
options = ['Head', 'Tail']
answer = input("Choose one (Head, Tail)")
result = random.choice(options)
print(result)
if answer == result:
    print("correct")
else:
    print("wrong")