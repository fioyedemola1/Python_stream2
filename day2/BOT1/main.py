from utilty.botFunc import speak, listen
from utilty.game import game

weather = lambda : speak()

skills = {
    'game': lambda : game(),
    'weather': lambda : weather(),
}



while True:
    resp = listen()

    if resp in skills:
        skills.get(resp)
    else:
        speak(' i dont know that one')