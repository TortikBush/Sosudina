###################################################################
# Меню Духа
###################################################################

screen dyx_menu(origin="default"):
    modal True
    add "images/Bg_choise.png"
    
    $ p = menu_params["dyx"].get(origin, menu_params["dyx"]["default"])

    add p["light"] at transform:
        pos p["light_pos"]
        anchor (0, 1.0)
        zoom p["light_zoom"]
        xzoom 0.9
        yzoom 0.9
        alpha 0.0
        pause 0.1
        linear 1.0 alpha 4

    add p["static_activ"] at transform:
        pos p["static_pos"]
        anchor (0.5, 0.5)
        zoom p["static_zoom"]

    add p["static"] at transform:
        pos p["static_pos"]
        anchor (0.5, 0.5)
        zoom p["static_zoom"]
        alpha 1
        linear 1 alpha 0

    add p["image"] at transform:
        pos p["pos"]
        anchor (0.5, 0.5)
        zoom p.get("image_zoom", 0.5)

    use info_layout(
        "ДУХ",
        "Дух - жизненная сила, топливо живого существа...",
        "dyx_menu"
    )