import random


# Rock paper scissors
def game():
    Choice = ('rock', 'paper', 'scissors')

    computer = random.choice(Choice)

    speak('let us play a game')
    speak('what is your choice')

    answ = listen()

    if answ == computer:
        print('its a draw')
