################################################################################
## Экран навигации
################################################################################

# game/screens/main_menu/navigation.rpy

# game/chapters.rpy

# game/chapters.rpy


# init python:

#     def clear_all():

#         for save in renpy.list_saved_games():
#             renpy.unlink_save(save[0])

#         persistent._clear()
#         renpy.save_persistent()
init python:

    if persistent.can_continue is None:
        persistent.can_continue = False

    def clear_all():

        for slot, *_ in renpy.list_saved_games():
            renpy.unlink_save(slot)

        persistent.can_continue = False



 



    # def continue_game():

    #     # 1. автосейв
    #     try:
    #         if renpy.can_load("1", page="auto"):
    #             renpy.load("1", page="auto")
    #             return
    #     except:
    #         pass

    #     # 2. обычные сейвы
    #     saves = renpy.list_saved_games()

    #     for s in saves:
    #         slot = s[0]

    #         try:
    #             renpy.load(slot)
    #             return
    #         except:
    #             continue

    #     renpy.notify("Нет сохранений")
    
    def has_any_save():

       
        # Есть ли автосейвы?
        if renpy.list_slots(r"^auto-\d+$"):
            return True

        # Есть ли обычные сейвы?
        if renpy.list_slots(r"^\d+-\d+$"):
            return True

        return False

    def continue_game():

        # Сначала самый новый автосейв
        slot = renpy.newest_slot(r"^auto-\d+$")

        if slot:
            renpy.load(slot)
            return

        # Потом самый новый обычный сейв
        slot = renpy.newest_slot(r"^\d+-\d+$")

        if slot:
            renpy.load(slot)
            return

        renpy.notify("Нет сохранений")

init python:

    def start_new_game():
        clear_all()
        store.hovered_button = None
        renpy.show_screen("character_select")

default hovered_button = None

# Быстрое меню (quick_menu.rpy)
default quick_menu_open = False
default quick_menu = True

default pref_tab = "screen"

# Выбор персонажа (character_select.rpy)
default hovered_character = None
default character_select = None

# Экран помощи (help.rpy)



default nav_buttons = [
    ("Сохранения", "save_menu"),
    ("Перейти к", "chapter_save"), 
    ("Аккаунт", "account"),  
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
        "Продолжить": {  
            "size": 135,
            "font": "fronts/Neothic.ttf",
            "offset": 0,
            "arrow": False
        },
        "Сохранения": {"offset": 600},
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


    # textbutton "Продолжить":
    #     xpos 2300
    #     ypos 870
    #     text_size 135
    #     text_font "fronts/Neothic.ttf"

    #     # action FileLoad(1, page="auto", confirm=False)
    #     action Function(continue_game)

    #     sensitive persistent.can_continue

    #     hovered SetVariable("hovered_button", "Продолжить")
    #     unhovered SetVariable("hovered_button", None)

    textbutton "Продолжить":
        xpos 2300
        ypos 870
        text_size 135
        text_font "fronts/Neothic.ttf"

        action Function(continue_game)

        sensitive has_any_save()

        hovered SetVariable("hovered_button", "Продолжить")
        unhovered SetVariable("hovered_button", None)
            
    
    
    textbutton "Начать игру":
        xpos 2300
        ypos 1100
        text_size nav_config["Начать игру"]["size"]

        if nav_config["Начать игру"]["font"]:
            text_font nav_config["Начать игру"]["font"]

            action Confirm(
            "Вы точно хотите начать игру заново?",
                Function(start_new_game),
                # SetVariable("hovered_button", None),
                # ShowMenu("character_select")
        )

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
    $ names = ["Сохранения", "Аккаунт", "Настройки", "Помощь", "Об игре","Выход"]

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