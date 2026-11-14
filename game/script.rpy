# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define Y = Character("You", color="#82140c")
define B = Character("Brother", color="#32201f")
define C = Character("Cousin", color="#1e0c82")
define F = Character("Best friend", color="#145109")
image cousin normal = "cousinnormal-removebg-preview.png"
image brothercandle = "bg brother-candle.png"

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
    scene bg kitchentable
    "Your cousin bumps into you with a plateful of Grandma's favorite cookies."
    show cousin normal
    C "Oh hey! Long time no see! How's the job?"
    menu: 
        "Good": 
            jump cousin2
        "Fine":
            jump cousin2
            
label cousin2:
    C "Oh that's good to hear. Lizzy's got a new job now as well, moved to a whole other continent and everything!"
    "You nod in acknowledgement and your cousin rushes off to arrange the cookies. The jug of milk is on the counter." 
    "Now the jug of milk is poisoned."
    jump aftermath

label bestfriend1:
    scene bg cuttingboard
    "Your best friend is cutting up apples in the kitchen. There's one more knife on the rack."
    show bestfriend normal
    F "What's up? Wanna help me cut up the fruit?"
    menu: 
        "Sure, but I'm going to finish up some stuff first.":
            jump bestfriend2 
        "Nah, I'm just inspecting the damascus steel.":
            jump bestfriend2 
label bestfriend2: 
    show bestfriend disappointed
    F "Fine by me then. We're still meeting up on Wednesday for game night, right? "
    "You nod and take the knife out of the block. It's heavy in your hands. You know what to do now."
    jump aftermath

label brother1:
    scene bg brothercandle
    "You walk into the living room to see your brother watching hell's kitchen"
    show brother normal
    B "This is a very good episode… Do you need something?"
    menu: 
        "Have you seen the candles?": 
            jump brother2a
        "It's a little dark in here isn't it?":
            jump brother2b
label brother2a: 
    B "Yeah they’re right here. How many do you need?"
    Y "Just give me all of them."
    B "Okay… just be careful. We don't want a fire during G-ma's birthday party, do we?"
    jump brother3
label brother2b: 
    B "Lets light something up"
    B "I have some candles. Do you want any?"
    Y "Just give me all of them"
    B "..."
    B "Okay..."
    jump brother3

label brother3: 
    hide brother normal
    "You exit the room"
    show bg black
    Y "Time to light this place up."
    "You light an absurd amount of candles"
     
    "You stand on the hill, watching the flames lick the sky."
    jump aftermath


label aftermath:

  