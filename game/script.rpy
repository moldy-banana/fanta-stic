# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Y = Character("You", color="#82140c")
define B = Character("Brother", color="#32201f")
define C = Character("Cousin", color="#1e0c82")
define F = Character("Best friend", color="#145109")



# The game starts here.

label start:
    play music "audio/Jazz at Mladost Club - Caravan.mp3"
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg bday

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # show eileen happy

    # These display lines of dialogue.

    "Everyone's here to celebrate Grandma's birthday. You have other motives "

    Y "Everyone is gathered here today... this might be my only chance. "
    menu: 
        "How should I do it?"

        "Poison the milk": 
            jump cousin1
        
        "Grab a knife":
            jump bestfriend1
        
        "Light the candles":
            jump brother1
    # This ends the game.

    return

label cousin1:
    scene bg table
    "Your cousin bumps into you with a plateful of Grandma's favorite cookies."
    C "Oh hey! Long time no see! How's the job?"
    menu: 
        "Good": 
            jump cousin2
        "Fine":
            jump cousin2
            
label cousin2:
    C "Oh that's good to hear. Lizzy's got a new job now as well, moved to a whole other continent and everything!"
    "You nod in acknowledgement and your cousin rushes off to arrange the cookies. The jug of milk is on the counter." 
    "Now the jug of milk is spiked."
    jump aftermath

label bestfriend1:
label brother1:

label aftermath:

  