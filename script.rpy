
define s = Character("Sam")
default sam_affection = 0

label start:

    scene bg room

    show sam blush

    s "I guess you like me"
menu: 

    "Yes, I do.": 
        $ sam_affection +1
    "No, I don't.":
        $ sam_affection -1
label ending_evaluation:
    if sam_affection == 1:
        jump sam_best_ending
    elif sam_affection == 0:
        jump sam_bad_ending

label sam_best_ending:
    s "I love you"
label sam_bad_ending: 
    s "I'll see you then"

    jump point_and_click 
