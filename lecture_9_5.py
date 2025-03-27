import random as r

def estimate(computer, user):
    if computer == user:
        return 0

    elif computer == "r":
        if user == "s":
            return -1
        else:
            return 1

    elif computer == "p":
        if user == "r":
            return -1
        else:
            return 1

    elif computer == "s":
        if user == "p":
            return -1
        else:
            return 1

def convertToString(result):
    if result == "r":
        return "Rock"
    elif result == "p":
        return "Paper"
    elif result == "s":
        return "Scissors"
    else:
        return -1

def main():
    user = None
    while True:
        user = input("Rock, Paper, Scissors! (r, p, s) ")
        if user in ["r", "p", "s"]:
            break
        else:
            print("Invalid input. Please try again.")

    computer = r.choice(["r", "p", "s"])
    result = estimate(computer, user)
    print("---------------<Result>-----------------")
    if result == 1:
        print("You Win! Computer chose", convertToString(computer))

    elif result == -1:
        print("You Lose! Computer chose", convertToString(computer))

    else:
        print("Withdrew! Computer chose", convertToString(computer))
    print("-----------------------------------------")
    again = input("Again? (y, n) ")
    if again == "y":
        main()
main()