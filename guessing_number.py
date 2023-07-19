import random

while True:
    num = random.randint(1, 10)

    while True:
        guess = int(input("Enter the number you have guessed:"))

        if guess == num:
            print("Hurray!! You have guessed it correctly.")

            another_guess = input("Want to make another guess? Yes or No\n").lower()
            if another_guess == 'yes':
                break
            else:
                print("Bye")
                print("Thank You <3")
                break
        else:
            print("OOPS!! Try again.")

    play_again = input("Want to play again? Yes or No\n").lower()
    if play_again != 'yes':
        print("Bye")
        print("Thank You <3")
        break