init python:
    collected_items = set()
    all_items = {"crowbar", "lotion", "facewash", "popsi", "lipgloss", "sledgehammer"}

    def dragged_func(dragged_items, dropped_on):
        if dropped_on is not None:
            if dropped_on.drag_name == "basket":
                dragged_items[0].snap(dropped_on.x, dropped_on.y, 0.5)
                collected_items.add(dragged_items[0].drag_name)
                renpy.restart_interaction()  # Force the screen to refresh
                

screen drag_drop:
    draggroup:
        # Only show if not collected
        if "crowbar" not in collected_items:
            drag:
                align(0.3, 0.43)
                drag_raise True
                drag_name "crowbar"
                dragged dragged_func
                image ("images/items/crowbar.png") zoom 1.2
        drag:
            align(0.9, 0.75)
            drag_raise True
            drag_name "basket"
            dragged dragged_func
            image ("images/items/basket.png") zoom 1.7
        if "lotion" not in collected_items:
            drag:
                align(0.2, 0.85)
                drag_raise True
                drag_name "lotion"
                dragged dragged_func
                image ("images/items/lotion.png") zoom 1.2
        if "facewash" not in collected_items:
            drag:
                align(0.4, 0.5)
                drag_raise True
                drag_name "facewash"
                dragged dragged_func
                image ("images/items/facewash.png") zoom 1.2
        if "popsi" not in collected_items:
            drag:
                align(0.5, 0.17)
                drag_raise True
                drag_name "popsi"
                dragged dragged_func
                image ("images/items/popsi.png") zoom 1.2
        if "lipgloss" not in collected_items:
            drag:
                align(0.6, 0.5)
                drag_raise True
                drag_name "lipgloss"
                dragged dragged_func
                image ("images/items/lipgloss.png") zoom 1.2
        if "sledgehammer" not in collected_items:
            drag:
                align(0.1, 0.25)
                drag_raise True
                drag_name "sledgehammer"
                dragged dragged_func
                image ("images/items/sledgehammer.png") zoom 1.2
    if collected_items >= all_items:
        textbutton "Finish Shopping" action Return() xpos 0.5 ypos 0.9 anchor (0.5, 0.5)
label shopp:
    call screen drag_drop
    return


