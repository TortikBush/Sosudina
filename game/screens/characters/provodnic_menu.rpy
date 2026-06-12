###################################################################
# Меню Проводника
###################################################################

screen provodnic_menu():
    modal True
    add "images/Bg_choise.png"

    add "images/light.png" at transform:
        pos (690, 0.949)
        anchor (0, 1.0)
        zoom 0.7
        xzoom 0.9
        yzoom 0.9
        alpha 0.0
        pause 0.1
        linear 1.0 alpha 4

    add "images/static_activ.png" at transform:
        pos (1100, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485

    add "images/static.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 1
        linear 1 alpha 0

    add "images/provodnic02.png" at transform:
        pos (1101, 700)  
        anchor (0.5, 0.5)
        zoom 0.5

    frame:
        xalign 0.5  
        xoffset 800  
        yalign 0.1
        background None
        
    use info_layout(
        "ПРОВОДНИК",
        "Проводник – это наш внутренний наставник...",
        "provodnic_menu"
    )