import random
import time

def guessing_game():
    try:
        player = input("Please enter your name: ")
        max_tries = 3
        max_rounds = 3
        total_score = 0
        rounds = 0

        print(f"\n ----- Welcome to the Guessing Game, {player}! ----- ")

        while rounds < max_rounds:
            correct_guess = random.randint(1, 100)
            tries = 0
            rounds += 1
            print(f"\n--- Round {rounds} ---")

            while tries < max_tries:
                print(f"\n----- Round {rounds}: Attempt {tries + 1} -----")
                start = time.time()
                try:
                    guess = int(input("Please guess a number between 1 and 100: "))
                except ValueError:
                    print("Invalid entry. Please enter a number.")
                    continue
                stop = time.time()
                time_taken = stop - start
                tries += 1

                if guess == correct_guess:
                    print("You guessed correctly!")

                    
                    if tries == 1:
                        points = 10
                        if time_taken < 5:
                            points += 10
                    elif tries == 2:
                        points = 7
                        if time_taken < 5:
                            points += 3
                    else:  
                        points = 5
                        if time_taken < 5:
                            points += 2

                    total_score += points
                    print(f"⏱Time taken: {round(time_taken, 2)} seconds")
                    print(f" You earned {points} points this round.")
                    break

                elif guess < correct_guess:
                    print("Too low, try again.")
                else:
                    print("Too high, try again.")

                if tries == max_tries:
                    print(f"You've used all your tries! The correct number was {correct_guess}.")
                    break

        print("\n🏁 ----- GAME OVER -----")
        print(f"Player: {player}")
        print(f"Your total score after {max_rounds} rounds is: {total_score} points.")
        print("Thanks for playing! ")

    except Exception as e:
        print("An error occurred:", e)


if __name__ == "__main__":
    guessing_game()
