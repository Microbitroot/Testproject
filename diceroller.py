import random

def roll_dice():
    """
    Simulates rolling a six-sided dice.
    Returns a random number between 1 and 6.
    """
    return random.randint(1, 6)

def main():
    num_rolls = int(input("Enter the number of times you want to roll the dice: "))

    for _ in range(num_rolls):
        result = roll_dice()
        print(f"Rolled: {result}")

if __name__ == "__main__":
    main()

