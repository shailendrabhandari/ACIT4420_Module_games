import random

def play():
    # Define difficulty seTTings: (min_num, max_num, max_attempts)
    difficulties = {
        'easy': (1, 10, 10),
        'medium': (1, 50, 8),
        'difficult': (1, 100, 6)
    }
    
    while True:
        # Prompt for difficulty
        print("Select difficulty level:")
        print("1. Easy (1-10, 10 attempts)")
        print("2. Medium (1-50, 8 attempts)")
        print("3. Difficult (1-100, 6 attempts)")
        
        try:
            choice = input("Enter 1, 2, or 3: ").strip()
            if choice == '1':
                level = 'easy'
            elif choice == '2':
                level = 'medium'
            elif choice == '3':
                level = 'difficult'
            else:
                raise ValueError("Invalid choice")
        except ValueError:
            print("Please enter 1, 2, or 3.")
            continue
        
        # Get difficulty settings
        min_num, max_num, max_attempts = difficulties[level]
        number = random.randint(min_num, max_num)
        attempts = 0
        
        print(f"\nI'm thinking of a number between {min_num} and {max_num}.")
        print(f"You have {max_attempts} attempts to guess it!")
        
        while attempts < max_attempts:
            try:
                guess = int(input("Take a guess: "))
                attempts += 1
                
                # Validate guess range
                if guess < min_num or guess > max_num:
                    print(f"Please guess a number between {min_num} and {max_num}.")
                    attempts -= 1  # Don't count invalid guesses
                    continue
                
                if guess == number:
                    result = f"Correct! You guessed {number} in {attempts} attempts."
                    break
                elif guess < number:
                    print("Too low!")
                else:
                    print("Too high!")
                    
            except ValueError:
                print("Please enter a valid number.")
                attempts -= 1  # do not count invalid inputs
        
        else:
            # IF max attempts reached
            result = f"Sorry, you've used all {max_attempts} attempts. The number was {number}."
        
        print(result)
        
        # Play again prompT
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            return result  # Return the last game's result for main.py