import random
def computer_guess(x):
    high=x
    low=1
    feedback=''
    while feedback!='c':
        if low!=high:
            guess=random.randint(low,high)
        else:
            guess=low
        feedback=input(f"Is {guess} correct(c) or high(h) or low(l)!....").lower()
        if feedback=='h':
            high=guess-1
        elif feedback=='l':
            low=guess+1
        elif feedback=='c':
            print(f"Your guessed number is{guess}")
x=int(input("Enter a number range"))
computer_guess(x)
