# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("")

init python:
    def drag_placed(drags, drop):
        if not drop:
            return

        store.draggable = drags[0].drag_name
        store.droppable = drop.drag_name

        return True

# The game starts here.

label inventory:

    scene black 

    hide screen drag_sample1A
    hide screen drag_sample1B
    call screen drag_sample2

    jump huh
    

screen drag_sample2:
    draggroup:
        drag:
            drag_name "circle"
            child "Note.png"
            xpos 100
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "triangle"
            child "Polaroid.png"
            xpos 400
            ypos 100
            draggable True
            droppable False
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "square"
            child "Album_.png"
            xpos 700
            ypos 100
            draggable True
            droppable True
            dragged drag_placed
            drag_raise True
        drag:
            drag_name "The Left Circle"
            xpos 0.1
            ypos 0.6
            child "Proof.png"
            draggable False
            droppable True
        drag:
            drag_name "The Right Circle"
            xpos 0.6
            ypos 0.6
            child "Proof.png"
            draggable False
            droppable True

