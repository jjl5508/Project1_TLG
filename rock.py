
while True:
    Question01 = input("What kind of movie do I like?:")
    answer = str(input())

    if answer == "Action":
        print("Congrats")
    else:
        print("Try Again!")

    play = input("Play again? (y/n): ")
    if play.lower() != "y":
        break
