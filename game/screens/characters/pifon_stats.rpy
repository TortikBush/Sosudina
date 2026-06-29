###################################################################
# Экран статистики Пифона
###################################################################

transform fade_in(delay=0.0):
    alpha 0.0
    pause delay
    linear 0.5 alpha 1.0

screen pifon_stats():
    modal True
    add "images/Bg_choise.png"

    frame:
        xalign 0.5
        xoffset 800
        yalign 0.1
        background None
        vbox:
            xsize 1000
            spacing 10
            text "ПИФОН":
                size 200
                color "#FFFFFF"
                outlines [(2, "#000000", 0, 0)]
                xalign 0.5
                at fade_in()
            text "особенность:":
                size 35
                color "#FFD700"
                outlines [(1, "#000000", 0, 0)]
                xalign 0.5
                at fade_in(0.5)
            text "Неконтролируемые видения прошлого и будущего":
                size 30
                color "#FFFFFF"
                outlines [(1, "#000000", 0, 0)]
                line_spacing 5
                xalign 0.5
                at fade_in(1.0)
            null height 200
            imagebutton:
                idle "images/knopka_vybrat.png"
                xalign 0.5
                action [
                    SetField(persistent, "can_continue", True),
                    Start()
                ]
                # action Start()

    if renpy.get_screen("pifon_stats"):
        add "images/light.png" at transform:
            pos (150, 0.95)
            anchor (0, 1.0)
            zoom 0.7
            xzoom 0.9
            yzoom 0.7
            alpha 0.0
            pause 2
            linear 1.0 alpha 4

    imagebutton:
        idle "ten01.png"
        hover "ten02.png" 
        pos (670, 1095)
        anchor (0.5, 0.5)
        action Show("ten_menu")  

    add "images/static_activ.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 0.0
        pause 0.5
        linear 1.0 alpha 1.0

    add "images/static.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 0.0
        pause 0.5
        linear 1.0 alpha 1.0

    imagebutton:
        idle "boby.png"
        hover "boby01.png"
        pos (1104, 1080)
        anchor (0.5, 0.5)
        focus_mask True 
        action Show("boby_menu")  

    imagebutton:
        idle "Provodnic.png"
        hover "Provodnic01.png"
        pos (1104, 400)
        anchor (0.5, 0.5)
        action Show("provodnic_menu") 

    imagebutton:
        idle "Dyx.png"
        hover "Dyx01.png"
        pos (1104, 705)
        anchor (0.5, 0.5)
        focus_mask True 
        action Show("dyx_menu")