import random

MIN = 1
MAX = 100

HARD_MODE = True


def player_guess():
    steps = 0
    computer = random.randint(MIN, MAX)

    while True:
        player = input(f"Enter a num btw {MIN}-{MAX} :")

        if player.isdigit() and MIN <= int(player) <= MAX:
            player = int(player)
            if player == computer:
                print(f"Yes! '{computer}' is the number")
                print(f"You figured it in {steps} tries")
                break
            elif player > computer:
                print("too high")
            else:
                print("too low")
        steps += 1

    return steps


step_c = 0


def computer_guess(player):
    low = MIN
    high = int(MAX)
    step = 0
    try:
        while True:
            computer = random.randint(low, high)
            print(f"is your num {computer} ? ")
            if player == computer:
                print(f"yay ! found it in {step} steps")
                break
            x = ["l", "h"]
            y = None
            while y not in x:
                y = input("too low(l),too high(h)? :").lower()
            if y == "l":
                low = computer + 1
            else:
                high = computer - 1
            step += 1
    except ValueError:
        print("You didn't gave the inputs correctly!")
        try_again = input("Do you wanna try again?[y/n] :").lower()
        if try_again == "y":
            computer_guess(player)

    return step


def computer_binary_search(l, key):
    global step_c
    mid = len(l) // 2

    if l[mid] == key:
        print(f"\nYay!,I found {l[mid]} in {step_c} step(s)")
        return step_c

    elif len(l) == 1 and l[mid] != key:
        print('Invalid Inputs were given!')

    choice = None

    while choice not in ['h', 'l']:
        choice = input(f"is your num {l[mid]} ?\ntoo high(h),too low(l): ").lower()

    if choice == "l":
        step_c += 1
        return computer_binary_search(l[mid:], key)
    else:
        step_c += 1
        return computer_binary_search(l[:mid + 1], key)


def check_winner(x, y):
    print(" ___~TRIES~____ ")
    print(f"| Player   | {x} |")
    print("+----------+---+")
    print(f"| Computer | {y} |")
    print(" -------------- ")
    if x == y:
        print("Its a tie!")
    elif x > y:
        print("COMPUTER WINS!")
    else:
        print("PLAYER WINS!")


def main():
    print("welcome to number guess game!")
    print("=============================\n")

    while True:
        print("guess the computer's number in less tries")
        x = player_guess()
        # x = steps taken by the player to find the number
        print("\nlet the computer guess your number in less tries")

        l = [i for i in range(MIN, MAX)]
        while True:
            player = input(f"Enter a num btw {MIN}-{MAX} :")
            if player.isdigit() and MIN <= int(player) <= MAX:
                player = int(player)
                break

        if HARD_MODE:
            y = computer_binary_search(l, player)  # binary_search_guess
        else:
            y = computer_guess(player)  # random guess

        # y = steps taken by the computer to find the number
        print()
        check_winner(x, y)

        play_again = input("Play again?(y/n): ").lower()
        if play_again != "y":
            print("Thank you")
            break


if __name__ == '__main__':
    main()
