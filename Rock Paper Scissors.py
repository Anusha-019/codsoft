import random

def get_user_choice():
    choices=['rock','paper','scissors']
    while True:
        user_choice=input("Enter your choice (rock, paper, scissors):").strip().lower()
        if user_choice in choices:
            return user_choice
        print("Invalid choice! Please choose a valid choice from the above")

def get_computer_choice():
    return random.choice(['rock','paper','scissors'])

def determine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        return "Tie"
    elif (user_choice=="rock" and computer_choice=="scissors") or (user_choice=="scissors" and computer_choice=="paper") or (user_choice=="paper" and computer_choice=='rock'):
        return "user"
    else:
        return "computer"

def display_results(user_choice,computer_choice,winner):
    print("You chose:",user_choice)
    print("Computer chose:",computer_choice)
    if winner=='Tie':
        print("It's a tie!")
    elif winner=='user':
        print("You win!")
    else:
        print("Computer wins!")
def main():
    user_score=0
    computer_score=0

    while True:
        user_choice=get_user_choice()
        computer_choice=get_computer_choice()
        winner=determine_winner(user_choice,computer_choice)
        display_results(user_choice,computer_choice,winner)
        if winner=='user':
            user_score+=1
        elif winner=='computer':
            computer_score+=1
        
        print(f" Score -> You:{user_score} | Computer: {computer_score}")

        play_again=input("Do you want to continue (yes/no):").strip().lower()
        if play_again!="yes":
            break
    print("Thankyou for playing!")

if __name__=="__main__":
    main()
