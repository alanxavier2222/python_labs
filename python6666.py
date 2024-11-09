import random

def roll_dice():
    return random.randint(1, 6)

def roll_simulator():
    rolls = int(input("How many times do you want to roll the dice? "))
    results = [roll_dice() for _ in range(rolls)]
    print(f"Results: {results}")
    print(f"Total: {sum(results)}")

if __name__ == "__main":
    roll_simulator()

