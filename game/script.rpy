# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Y = Character("You", color="#82140c")
define B = Character("Brother", color="#32201f")
define C = Character("Cousin", color="#1e0c82")
define F = Character("Best friend", color="#145109")



# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bday

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "Everyone’s here to celebrate Grandma’s birthday. You have other motives "

    Y "Everyone is gathered here today... this might be my only chance. How should I do it?"

    # This ends the game.

    return
