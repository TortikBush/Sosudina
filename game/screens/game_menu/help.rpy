################################################################################
## Экран помощи
################################################################################

screen help():
    tag menu
    default device = "keyboard"
    use game_menu(_("Помощь"), scroll="viewport"):
        style_prefix "help"
        vbox:
            spacing 45
            hbox:
                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                textbutton _("Мышь") action SetScreenVariable("device", "mouse")
                if GamepadExists():
                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")
            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help

screen keyboard_help():
    hbox:
        label _("Enter или Пробел")
        text _("Прохождение диалогов")
    hbox:
        label "S"
        text _("Открывает настройки")
    hbox:
        label "H"
        text _("Открывает историю")
    hbox:
        label "V"
        text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.")
    hbox:
        label "Cntrl + S"
        text _("Сохранение")

screen mouse_help():
    hbox:
        label _("Клик колёсиком")
        text _("Скрывает интерфейс пользователя.")

screen gamepad_help():
    hbox:
        label _("Правый триггер\nA/Нижняя кнопка")
        text _("Прохождение диалогов, активация интерфейса.")
    hbox:
        label _("Левый Триггер\nЛевый Бампер")
        text _("Откат назад по сюжету игры.")
    hbox:
        label _("Правый бампер")
        text _("Откатывает предыдущее действие вперёд.")
    hbox:
        label _("Крестовина, Стики")
        text _("Навигация по интерфейсу.")
    hbox:
        label _("Старт, Гид, B/Правая кнопка")
        text _("Вход в игровое меню.")
    hbox:
        label _("Y/Верхняя кнопка")
        text _("Скрывает интерфейс пользователя.")
    textbutton _("Калибровка") action GamepadCalibrate()