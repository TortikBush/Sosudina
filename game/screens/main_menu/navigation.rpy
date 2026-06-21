################################################################################
## Экран навигации
################################################################################

# game/screens/main_menu/navigation.rpy




default hovered_button = None

# Быстрое меню (quick_menu.rpy)
default quick_menu_open = False
default quick_menu = True

# Настройки (preferences.rpy)
default pref_tab = "screen"

# Выбор персонажа (character_select.rpy)
default hovered_character = None
default character_select = None

# Экран помощи (help.rpy)



default nav_buttons = [
    ("История", "history"),
    ("Перейти к", "chapter_save"), 
    ("Аккаунт", "save_menu"),  
    ("Настройки", "preferences"),
    ("Помощь", "help"),
    ("Об игре", "about"),
    ("Выход", None),
]

init python:
    nav_config = {
        "Начать игру": {
            "size": 135,
            "font": "fronts/Neothic.ttf",
            "offset": 0,
            "arrow": False
        },
        "Продолжить": {  # ← ДОБАВИТЬ
            "size": 135,
            "font": "fronts/Neothic.ttf",
            "offset": 0,
            "arrow": False
        },
        "История": {"offset": 600},
        "Аккаунт": {"offset": 615},
        "Настройки": {"offset": 515},
        "Помощь": {"offset": 610},
        "Об игре": {"offset": 630},
        "Выход": {"offset": 650,"arrow": True}, 
        "default": {
            "size": 90,
            "font": None,
            "offset": 600,
            "arrow": True
        }
    }



screen navigation():
    add "images/Icon.png":
        xpos 110
        ypos 100
        zoom 0.7  

    add "images/line_mainmenu.png":
        xpos 2200
        ypos 1000
        zoom 0.7 


    textbutton "Продолжить":
        xpos 2300
        ypos 870
        text_size 135
        text_font "fronts/Neothic.ttf"
        action FileLoad(1, page="auto", confirm=False)
        hovered SetVariable("hovered_button", "Продолжить")
        unhovered SetVariable("hovered_button", None)
        sensitive True
    # textbutton "Продолжить":
    #     xpos 2300
    #     ypos 870
    #     text_size 135
    #     text_font "fronts/Neothic.ttf"
    #     action If(
    #         renpy.can_load("autosave"),
    #         FileLoad("autosave", confirm=False),
    #         None
    #     )
    #     hovered SetVariable("hovered_button", "Продолжить")
    #     unhovered SetVariable("hovered_button", None)
    #     # sensitive renpy.can_load("autosave")
    #     sensitive True
    # else:
    #     textbutton "Продолжить":
    #         xpos 2300
    #         ypos 870
    #         text_size 135
    #         text_font "fronts/Neothic.ttf"
    #         action None
    #         sensitive False
    #         text_color "#666666"
    
    textbutton "Начать игру":
        xpos 2300
        ypos 1100
        text_size nav_config["Начать игру"]["size"]
        if nav_config["Начать игру"]["font"]:
            text_font nav_config["Начать игру"]["font"]
        action ShowMenu("character_select")
        hovered SetVariable("hovered_button", "Начать игру")
        unhovered SetVariable("hovered_button", None)
        
    vbox:
        style_prefix "navigation"
        xpos 3250
        yalign 0.93
        xanchor 1.0
        spacing gui.navigation_spacing

        for name, action_name in nav_buttons:
            $ base = nav_config["default"]
            $ custom = nav_config.get(name, {})
            $ cfg = dict(base, **custom)

            if name == "Выход":
                $ btn_action = Quit(confirm=False)
            else:
                $ btn_action = [SetVariable("hovered_button", None), ShowMenu(action_name)]

            textbutton _(name):
                action btn_action
                text_size cfg["size"]

                if cfg["font"]:
                    text_font cfg["font"]

                if cfg.get("arrow", True):
                    hovered SetVariable("hovered_button", name)
                    unhovered SetVariable("hovered_button", None)
            # $ base = nav_config["default"]
            # $ custom = nav_config.get(name, {})
            # $ cfg = dict(base, **custom)

            # if name == "Выход":
            #     $ btn_action = Quit(confirm=False)
            # elif name == "Продолжить":
            #     if renpy.can_load("autosave-LT1"):
            #         $ btn_action = FileLoad("autosave-LT1",confirm=False)
            #     else:
            #         $ btn_action = None
            # else:
            #     $ btn_action = [SetVariable("hovered_button", None), ShowMenu(action_name)]

            # # if name == "Продолжить" and not renpy.can_load("autosave-LT1"):
            # #     textbutton _(name):
            # #         action None
            # #         sensitive False
            # #         text_size cfg["size"]
            # #         if cfg["font"]:
            # #             text_font cfg["font"]
            # #         text_color "#666666"
            # # else:
            #     textbutton _(name):
            #         action btn_action
            #         text_size cfg["size"]
            #         if cfg["font"]:
            #             text_font cfg["font"]
            #         if cfg.get("arrow", True):
            #             hovered SetVariable("hovered_button", name)
            #             unhovered SetVariable("hovered_button", None)

    if hovered_button:
        use arrow_screen(button_name=hovered_button)

screen arrow_screen(button_name=""):
    $ names = ["История", "Аккаунт", "Настройки", "Помощь", "Об игре","Выход"]

    if button_name in names:
        $ index = names.index(button_name)

        add "images/arrow.png":
            xpos 3350
            ypos 1300 + index * 130
            zoom 0.8
            at arrow_transform

transform arrow_transform:
    alpha 0.0 zoom 0.5
    linear 0.2 alpha 1.0 zoom 0.8
    on hide:
        linear 0.15 alpha 0.0 zoom 0.5