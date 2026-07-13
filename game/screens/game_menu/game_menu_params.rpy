# game/menu_params.rpy

init python:
    # Параметры для всех меню (изначальные)
    menu_params = {
        "ten": {
            "default": {
                "light": "images/light.png",
                "image": "images/ten01.png",
                "hover": "images/ten02.png",
                "static_activ": "images/static_activ.png",
                "static": "images/static.png",
                "light_pos": (850, 0.95),
                "light_zoom": 0.7,
                "pos": (670, 1095),
                "static_pos": (1100, 1091),
                "static_zoom": 0.485,
                "image_zoom": 1,      # ← для основной
                "hover_zoom": 1  
            },
            "account": {
                "light": "images/light.png",
                "image": "images/teny_account.png",
                "hover": "images/redy_teny.png",
                "static_activ": "images/static_activ_account.png",
                "static": "images/boddy_for_account.png",
                "light_pos": (850, 0.95),
                "light_zoom": 0.5,
                
                "pos": (570, 1250),
                "static_pos": (1300, 1221),
                "static_zoom": 0.885,
                
                "image_zoom": 0.5
                # "hover_zoom": 0.3
            }
        },
        "boby": {
            "default": {
                "image": "images/boby02.png",
                "static": "images/static.png",
                "pos": (1104, 1091),
                "static_pos": (1104, 1091),
                "static_zoom": 0.485,
                "image_zoom": 0.485
            },
            "account": {
                "image": "images/boddy_redy.png",
                "static": "images/boddy_for_account.png",
                "pos": (1300, 1221),
                "static_pos": (1300, 1221),
                "static_zoom": 0.885,
                "image_zoom": 0.885
            }

        },
         "dyx": {
            "default": {
                "light": "images/light.png",
                "image": "images/Dyx02.png",
                "static_activ": "images/static_activ.png",
                "static": "images/static.png",
                "light_pos": (690, 0.949),
                "light_zoom": 0.7,
                "pos": (1101, 1050),
                "static_pos": (1100, 1091),
                "static_zoom": 0.485,
                "image_zoom": 0.5
            },
            "account": {
                "light": "images/light.png",
                "image": "images/dyx_account.png",
                "static_activ": "images/static_activ_account.png",
                "static": "images/boddy_for_account.png",
                "light_pos": (540, 0.999),
                "light_zoom": 1.3,
                "pos": (1305, 1155),
                "static_pos": (1300, 1221),
                "static_zoom": 0.885,
                "image_zoom": 0.885
            }


        },
         "provodnic": {
                "default": {
                    "light": "images/light.png",
                    "image": "images/provodnic02.png",
                    "static_activ": "images/static_activ.png",
                    "static": "images/static.png",
                    "light_pos": (690, 0.949),
                    "light_zoom": 0.7,
                    "pos": (1101, 700),
                    "static_pos": (1100, 1091),
                    "static_zoom": 0.485,
                    "image_zoom": 0.5
                },
                "account": {
                    "light": "images/light.png",
                    "image": "images/Provodnik_account.png",
                    "static_activ": "images/static_activ_account.png",
                    "static": "images/boddy_for_account.png",
                    "light_pos": (540, 0.999),
                    "light_zoom": 1.3,
                    "pos": (1305, 1305),
                    "static_pos": (1300, 1221),
                    "static_zoom": 0.885,
                    "image_zoom":  0.885
                }
         
            }
        }
    