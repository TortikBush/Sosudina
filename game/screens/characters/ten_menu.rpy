###################################################################
# Меню Тени
###################################################################

screen ten_menu(origin="default"):
    modal True
    add "images/Bg_choise.png"
    
    $ p = menu_params["ten"].get(origin, menu_params["ten"]["default"])

    add p["light"] at transform:
        pos p["light_pos"]
        anchor (0, 1.0)
        zoom p["light_zoom"]
        xzoom p["light_zoom"]
        yzoom p["light_zoom"]
        alpha 0.0
        pause 0.1
        linear 1.0 alpha 4

    add p["image"] at transform:
        pos p["pos"]
        anchor (0.5, 0.5)
        zoom p.get("image_zoom", 1.0)
    
    add p["hover"] at transform:
        pos p["pos"]
        anchor (0.5, 0.5)
        zoom p.get("image_zoom", 1.0)
    
    add p["static_activ"] at transform:
        pos p["static_pos"]
        anchor (0.5, 0.5)
        zoom p["static_zoom"]
    
    add p["static"] at transform:
        pos p["static_pos"]
        # pos (1104, 1091)
        anchor (0.5, 0.5)
        zoom p["static_zoom"]
        
        alpha 1
        linear 1 alpha 0

    use info_layout(
        "ТЕНЬ",
        "это наше подсознание, оно формируется из опыта, который мы не можем или не хотим осознавать...",
        "ten_menu"
    )