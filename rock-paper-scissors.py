import random
player1_points=0
player2_points=0
computer_points=0

def get_choice(player_name):
  choice=input(f"{player_name}Pick between rock, paper or scissors").lower()
  return choice

def decide_winner(p1, p2):
    if p1 == p2:
        return "tie"
    elif (
        (p1 == "rock" and p2 == "scissors") or
        (p1 == "paper" and p2 == "rock") or
        (p1 == "scissors" and p2 == "paper")
    ):
        return "player1"
    else:
        return "player2"



while True:
  print("\n----Rock,Paper and Scissors Game, what would you like to do?")
  print("1.Play vs another player")
  print("2.Play vs computer")
  print("3.Exit")
  user=input("Enter your choice; 1/2/3:")
  if user=="3":
    print("Goodbye")
    break

  elif user== "1":

        player = get_choice("Player")
        computer = random.choice(["rock", "paper", "scissors"])

        print(f"Computer chose: {computer}")

        result = decide_winner(player, computer)

        if result == "tie":
            print("It's a tie!")
        elif result == "player1":
            print("You win!")
            player1_points += 1
        else:
            print("Computer wins!")
            computer_points += 1

  elif user == "2":
      
        player1 = get_choice("Player 1")
        player2 = get_choice("Player 2")

        result = decide_winner(player1, player2)

        if result == "tie":
            print("It's a tie!")
        elif result == "player1":
            print("Player 1 wins!")
            player1_points += 1
        else:
            print("Player 2 wins!")
            player2_points += 1

  else:
        print("Invalid choice")

    
print("\n Scoreboard:")
print(f"Player 1: {player1_points}")
print(f"Player 2: {player2_points}")
print(f"Computer: {computer_points}")