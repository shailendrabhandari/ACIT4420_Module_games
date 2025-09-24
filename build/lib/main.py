from games.rock_paper_scissors import play as rps_play
from games.guess_the_number import play as gtn_play
from games.tic_tac_toe import play as ttt_play

def main():
    print("Welcome to the ACIT Game Module!")
    print("Choose a game to play:")
    print("1. Rock, Paper, Scissors")
    print("2. Guess the Number")
    print("3. Tic-Tac-Toe")
    
    choice = input("Enter the number of the game you want to play (1-3): ").strip()
    
    if choice == '1':
        print(rps_play())
    elif choice == '2':
        print(gtn_play())
    elif choice == '3':
        print(ttt_play())
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()