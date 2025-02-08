## START
label point_and_click:
    scene bg peach
    "You are in \"label start\""
    call screen zeil_learnings_logo

label end: 
    "You are in \"label end\""
    return

#############################################################################################
## IMAGE BUTTON
screen zeil_learnings_logo: 
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        idle "button_static.png"
        hover "button_hover.png"
        action [Hide("displayTextScreen"), Jump("end")]

        hovered Show("displayTextScreen", 
            displayText = "The logo is hovered! (click to end)") 
        unhovered Hide("displayTextScreen")  