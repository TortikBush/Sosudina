

# Персонажи
define p = Character("Пифон", color="#c8c8ff", window_style = "right_window")
define L = Character("Ламия", color="#ff635e", window_style = "left_window",namebox_style="left_namebox")




# Изображения таро 
image lami = "lami_taro.png"
image exi = "exi_taro.png"
image pifi = "pifon_taro.png"
image Lami_def = "Lami_def.png"


# Начало игры
label start:

    scene livingroom
    
    show pifon_book at left

    p "Что значит нет продолжения?"

    show Lami_def at right

    L "Ну вот так, я не смогла следующую книгу найти"

    L "Скорее всего при переезде забыли"

    show pifon_book at left

    p "И как я узнаю кто убийца?"

    show Lami_def at right

    L "Можешь использовать свои видения"

    show pifon_book at left

    p "Очень смешно"


# game/script.rpy

##label start:
  
    jump chapter_1

# Глава 1: Анте приносит пойманный дух
label chapter_1:
    scene bg_forest
    "Анте приносит пойманный дух..."
    
    $ complete_chapter("chapter_1")
    jump chapter_2

# Глава 2: Ритуал
label chapter_2:
    scene bg_temple
    "Ритуал начинается..."
    
    $ complete_chapter("chapter_2")
    jump chapter_3

# Глава 3: разговор Анте и Пифона
label chapter_3:
    scene bg_clearing
    
    menu:
        "Что скажешь?"
        "Да":
            "Анте соглашается."
        "Нет":
            "Анте отказывается."
    
    $ complete_chapter("chapter_3")
    jump chapter_4

# Глава 4: видение
label chapter_4:
    scene bg_vision
    "Пифон видит странное видение..."
    
    $ complete_chapter("chapter_4")
    jump chapter_5

# Глава 5: интерактив
label chapter_5:
    "интерактив..."
    
    $ complete_chapter("chapter_5")
    jump chapter_6

# Глава 6: Ехидна приносит письмо
label chapter_6:
    "Ехидна приносит письмо..."
    
    $ complete_chapter("chapter_6")
    jump chapter_7

# Глава 7: поездка
label chapter_7:
    "поездка..."
    
    $ complete_chapter("chapter_7")
    jump chapter_8

# Глава 8: разговор Пифона и Ламии
label chapter_8:
    "разговор Пифона и Ламии..."
    
    $ complete_chapter("chapter_8")
    jump end_game

label end_game:
    "Конец игры"
    return