print("Winning Rules of  Rock paper scissor game as: \n"
      + "Rock vs paper->paper wins \n"
      + "Rock vs scissors->Rock wins \n"
      + "paper vs scissors->scissors wins \n")

user1=input("enter your choice(rock,paper,scissors):")
user2=input("enter your choice(rock,paper,scissors):")
print(f"\nuser1 chose {user1}, user2 chose {user2}.\n")
def rps(user1,user2):
    if user1 ==user2:
        print(f"Both players selected {user1}. It's a tie!")
    elif user1 == "rock":
        if user2 == "scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user1 == "paper":
        if user2 == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user1 == "scissors":
        if user2 == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

print(rps(user1,user2))