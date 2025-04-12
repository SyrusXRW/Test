screen inventory_display_toggle:
    zorder 92
    imagebutton:
            xalign 1.0
            yalign 0.0
            auto "inventory_%s.png"
            action ToggleScreen("inventory_item_description")
    on "hide" action Hide("inventory_item_description")


default item_descriptions = {"note" : "a mysterious note"}
default inventory_items = []
default item_description = ""

# style inv_button is frame:
#     xsize 200
#     ysize 100

# style inv_button_text:
#     xalign 0.5
#     yalign 0.5

# style inv_image:
#     xalign 0.5
#     yalign 0.5

screen inventory_item_description:
    image "#3d3d3dff"
    # use this based on your preference
    modal True
    window:
        background "#aaaaaaff"
        xsize 600
        ysize 150
        xalign 0.5
        yalign 0.1
        text item_description:
            xfill True
            yfill True
#Above is for description text, Below is Items 
    frame:
        background "#9999ff00"
        xsize 1290
        ysize 600
        xalign 0.5
        yalign 0.7
        hbox:
            box_wrap True
            box_wrap_spacing 10
            spacing 10
            xoffset 10
            yoffset 20
            style_prefix "inv"
            for item in inventory_items:
                textbutton item:
                    action SetVariable("item_description", item_descriptions.get(item))

    on "hide" action SetVariable("item_description", "")