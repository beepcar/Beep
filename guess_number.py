import random
input("Welcome to guess_number Game!")
guess_number = 0
guess_number = random.randint(0 , 100)
level_play = input("choose a difficulty. Type 'easy' or 'hard':")
if level_play == "easy":
    def easy_play():
            input("you have [10]attempts to guess the number. Prss Enter")
            easy_play
            for i in range(10):
                i = 9
                number_user = int(input("Make a guess:"))
                if number_user == guess_number:
                    print("You are Win")
                    break
                elif number_user > guess_number:
                    print(f"Too high.,You have a attempts:{i}")
                    return i -1
                elif number_user < guess_number:
                    print(f"Too Low . You have attempts:{[i]}")
                if i == -1:
                    print("Last Try")
                if i == 0:
                    print(f"You Loss ,guess number is: {guess_number}")
if level_play == "hard":
    def hard_play():
            input("you have [5]attempts to guess the number. Prss Enter")
            for i in range(5):
                i -= 4
                number_user = int(input("Make a guess:"))
                if number_user == guess_number:
                    print("You are Win")
                    break
                if number_user > guess_number:
                    print(f"Too high.You have a attempts:{[i]}")
                if number_user < guess_number:
                    print(f"Too Low . You have attempts:{[i]}")
                if i == -1:
                    print("Last Try")
                if i == 0:
                    print(f"You Loss ,guess number is: {guess_number}")
    hard_play()