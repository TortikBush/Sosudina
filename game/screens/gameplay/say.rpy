################################################################################
## Экран разговора
################################################################################

init python:
    config.character_id_prefixes.append('namebox')

screen say(who, what):
    key "mouseup_1" action [SetVariable("quick_menu_open", False), Return()]
    window:
        id "window"

        
        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"
        text what id "what"

    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0