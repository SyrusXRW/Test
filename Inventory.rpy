screen inventory_display_toggle:
    window:
        imagebutton:
            xalign 0.05
            yalign 0.1
            auto "inventory_%s.png"
            action ToggleScreen("inventory_item_description")

    on "hide" action Hide("inventory_item_description")


default item_descriptions = {"Note" : "a clue to where to"}
default inventory_items = [0]
default item_description = "Blank"

style inv_button is frame:
    xsize 200
    ysize 100

style inv_button_text:
    xalign 0.5
    yalign 0.5

screen inventory_item_description:
    # use this based on your preference
    modal True
    window:
        background "#AAA9"
        xsize 600
        ysize 150
        xalign 0.5
        yalign 0.1
        text item_description:
            xfill True
            yfill True

    window:
        background "#99F9"
        xsize 1290
        ysize 600
        xalign 0.5
        yalign 0.7
        hbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 20
            yoffset 20
            style_prefix "inv"
            for item in inventory_items:
                textbutton item:
                    action SetVariable("item_description", item_descriptions.get(item))
                    selected False


    on "hide" action SetVariable("item_description", "")