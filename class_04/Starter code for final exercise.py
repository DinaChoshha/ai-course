import random

class RockPaperScissors:
    def __init__(self, rounds_to_win=3):
        self.choices = ["rock", "paper", "scissors"]
        self.rounds_to_win = rounds_to_win
        self.user_score = 0
        self.computer_score = 0

    def get_user_choice(self):
        while (True):
            choice = input("Enter rock, paper, or scissors: ").lower()
            if choice in self.choices:
                return choice
            print("Invalid choice. Please try again.")

    def get_computer_choice(self):
        return random.choice(self.choices)

    def decide_winner(self, user, computer):
        # check if tie.
        if user == computer:
            return "tie"

        # if there is not tie, check who won.
        wins_against = {"rock": "scissors", "scissors": "paper", "paper": "rock"}

        if wins_against[user] == computer:
            self.user_score += 1
            return "user"
        else:
            self.computer_score += 1
            return "computer"
 
    def play(self):
        print(f"Welcome to Rock-Paper-Scissors! First to {self.rounds_to_win} wins.")
        # TODO: loop until someone wins enough rounds
        while 0 < self.rounds_to_win:
            self.rounds_to_win -= 1

            # Get choices
            user_choice = self.get_user_choice()
            computer_choice = self.get_computer_choice()

            # Display choices and current score
            print(f"Computer chose: {computer_choice}")
            winner = self.decide_winner(user_choice, computer_choice)
            print(f"Score - You: {self.user_score}, Computer: {self.computer_score}\n")

        print("Game over!")

        # Announce the overall winner
        if self.computer_score == self.user_score:
            print("It's a tie!")
        elif self.computer_score <= self.user_score:
            print("Congratulations! You won the game!")  
        else:
            print("The computer won the game. Better luck next time!")

# Run the game
game = RockPaperScissors(rounds_to_win=3)
game.play()