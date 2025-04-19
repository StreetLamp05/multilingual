"""
8. Guess the Number Game
- [ ] Use `random.randint()` to generate number
- [ ] Get user input and give feedback
- [ ] Track number of attempts
"""

import random

def main():
    random_num = random.randint(1, 100)
    guess: int = -1
    count = 0
    print("Guess the Number Game")
    print("=====================")
    while guess != random_num:
        guess = int(input("Guess the number between 1 and 100: "))
        if guess not in range(1,100): # edgecase
            print("Please enter a number between 1 and 100")
        elif guess == random_num: #edgecase
            print("Congratulations, you guessed the number in ", count, "tries!")
        else:
            if guess < random_num:
                print("too low!")
            elif guess > random_num:
                print("too high!")
        count += 1

if __name__ == '__main__':
    main()