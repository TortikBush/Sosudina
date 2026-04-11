# Персонажи
define p = Character("Пифон", color="#c8c8ff")
define L = Character("Ламия", color="#ff635e")

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



    
 

    
