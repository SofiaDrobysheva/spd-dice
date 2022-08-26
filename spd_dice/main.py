import typer
import random


app = typer.Typer()


@app.callback()
def callback():
    """
    A dice or two, that's it. 
    """

@app.command()
def roll():
    """
    Roll one dice.
    """
    for i in range(1):
        side = random.randint(1, 6)
        print('[',side,']')


@app.command()
def double():
    """
    Roll two dices.
    """
    for i in range(2):
        side = random.randint(1, 6)
        print('[',side,']')
