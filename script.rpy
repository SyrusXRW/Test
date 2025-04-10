
define s = Character("Marco")
define a = Character("Alexi")
default alexi_affection = 0 

image Streets = "Streets.PNG" 
#to define images have lowercase 
#image Insert name = "File name.png"

#This will be a way to show all the differnet coding ways 

label start:
    show screen inventory_display_toggle
    show Streets

    show marco sprite at truecenter 
    #The Game has different ways to position things for characters it's at "Truecenter, Left, Right"

    show alexi sprite at left
    
    $ inventory_items.append("note")

    s "We got a clue"
    a "We should probably see the next clue"

menu:
    "Any clue where to?": 
        $ alexi_affection +1
    "I think we shouldn't": 
        a "I see..."


label ending_evaluation:
    if alexi_affection == 1:
        jump sam_best_ending
    else: 
        jump sam_bad_ending

label sam_best_ending:
    a "I think we can go to the Library"
label sam_bad_ending: 
    a "Let's head back then"

label huh: 
    "did it work?"

    return 
