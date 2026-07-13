###################################################################
# Меню Тела
###################################################################

screen boby_menu(origin="default"):
    modal True
    add "images/Bg_choise.png"
    
    $ p = menu_params["boby"].get(origin, menu_params["boby"]["default"])

    add p["image"] at transform:
        pos p["pos"]
        anchor (0.5, 0.5)
        zoom p.get("image_zoom", 0.5)
        alpha 1
        linear 0 alpha 1

    add p["static"] at transform:
        pos p["static_pos"]
        anchor (0.5, 0.5)
        zoom p["static_zoom"]
        alpha 1
        linear 1 alpha 0

    use info_layout(
        "ТЕЛО",
        "Тело – это сосуд, сотканный из плоти, металла или иной материи...",
        "boby_menu"
    )