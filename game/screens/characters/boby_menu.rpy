###################################################################
# Меню Тела
###################################################################

screen boby_menu():
    modal True
    add "images/Bg_choise.png"

    add "images/boby02.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 1
        linear 0 alpha 1

    add "images/static.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 1
        linear 1 alpha 0

    use info_layout(
        "ТЕЛО",
        "Тело – это сосуд, сотканный из плоти, металла или иной материи...",
        "boby_menu"
    )