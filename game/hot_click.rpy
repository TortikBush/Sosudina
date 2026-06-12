init python:
    # 1. Убираем ESC из списка клавиш, открывающих меню
    #    Используем try/except на случай, если клавиши там нет, чтобы избежать ошибки.
    try:
        config.keymap['game_menu'].remove('K_ESCAPE')
    except ValueError:
        pass # Клавиша и так удалена, ничего делать не нужно

    # 2. Добавляем ESC в список клавиш, переключающих полноэкранный режим
    #    Сначала проверяем, не добавлена ли она уже, чтобы не было дублей.
    if 'K_ESCAPE' not in config.keymap['toggle_fullscreen']:
        config.keymap['toggle_fullscreen'].append('K_ESCAPE')

init python:
    # Безопасно удаляем клавишу S (скриншот)
    if 'noshift_K_s' in config.keymap['screenshot']:
        config.keymap['screenshot'].remove('noshift_K_s')
    if 's' in config.keymap['screenshot']:
        config.keymap['screenshot'].remove('s')

init python:
    # Убираем открытие меню по правой кнопке мыши
    try:
        config.keymap['game_menu'].remove('mouseup_3')
    except ValueError:
        pass
    
    # Убираем открытие меню по двойному клику (если есть)
    try:
        config.keymap['game_menu'].remove('K_ESCAPE')
    except ValueError:
        pass
    
    # Убираем открытие меню по кнопке "Start" на геймпаде
    try:
        config.keymap['game_menu'].remove('joy_start')
    except ValueError:
        pass