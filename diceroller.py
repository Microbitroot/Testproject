import random

def roll_dice():
    """
    Simulates rolling a six-sided dice.
    Returns a random number between 1 and 6.
    """
    return random.randint(1, 6)

def main():
    try:
        num_rolls = int(input("Enter the number of times you want to roll the dice: "))
        for _ in range(num_rolls):
            result = roll_dice()
            print(f"Rolled: {result}")
    except EOFError:
        print("No input was provided.")
    except ValueError:
        print("Please enter a valid integer.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

