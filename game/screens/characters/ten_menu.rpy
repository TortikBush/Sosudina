###################################################################
# Меню Тени
###################################################################

screen ten_menu():
    modal True
    add "images/Bg_choise.png"

    add "images/light.png" at transform:
        pos (850, 0.95)
        anchor (0, 1.0)
        zoom 0.7
        xzoom 0.7
        yzoom 0.7
        alpha 0.0
        pause 0.1
        linear 1.0 alpha 4

    add "images/ten01.png" at transform:
        pos (670, 1095)
        anchor (0.5, 0.5)
    add "images/ten02.png" at transform:
        pos (670, 1095)
        anchor (0.5, 0.5)
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

    use info_layout(
        "ТЕНЬ",
        "это наше подсознание, оно формируется из опыта, который мы не можем или не хотим осознавать...",
        "ten_menu"
    )