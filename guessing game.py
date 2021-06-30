import random
answer = random.randint(1,100)
dif = (input("Choose either easy, medium, or hard: ")).lower()
if (dif == "easy"):
    tries = 15
if (dif == "medium"):
    tries = 10
if (dif == "hard"):
    tries = 6
user_input = -1
while (user_input != answer and tries > 0):
    print("The number of tries you have left is " + str(tries))
    user_input = int(input("Guess a number from 1 to 100: "))
    if (user_input == answer):
        print("You win!")
    elif (user_input > answer):
        print("The answer is less than the answer you chose")
    elif (user_input < answer):
        print("The answer is greater than the answer you chose")
    tries = tries -1
if (user_input != answer):
    print("You lose.")
    print("The answer was " + str(answer))
