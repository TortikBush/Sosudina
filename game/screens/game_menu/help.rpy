################################################################################
## Экран помощи
################################################################################

screen help():
    tag menu

    default help_tab = "keyboard"

    use game_menu(_("Помощь"), scroll="viewport"):

        hbox:
            xalign 0.0
            yalign 0.4
            spacing 50
            
            vbox:
                xalign 0.0  
                xoffset 50  
                yalign 1  
                spacing 40  
                
                button:
                    style "tab_button"
                    action SetScreenVariable("help_tab", "keyboard")
                    
                    if help_tab == "keyboard":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Клавиатура"):
                            style "tab_button_text_active"
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Клавиатура"):
                            style "tab_button_text"
                
                button:
                    style "tab_button"
                    action SetScreenVariable("help_tab", "mouse")
                    
                    if help_tab == "mouse":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Мышь"):
                            style "tab_button_text_active"
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Мышь"):
                            style "tab_button_text"
                
                button:
                    style "tab_button"
                    action SetScreenVariable("help_tab", "gamepad")
                    
                    if help_tab == "gamepad":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Геймпад"):
                            style "tab_button_text_active"
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Геймпад"):
                            style "tab_button_text"
            
            fixed:
                xsize 1800
                ysize 800
                xalign 0.0
                yalign 0.5
                
                if help_tab == "keyboard":
                    use keyboard_help
                elif help_tab == "mouse":
                    use mouse_help
                elif help_tab == "gamepad":
                    use gamepad_help
                else:
                    use keyboard_help

screen keyboard_help():
    vbox:
        spacing 30
        xoffset 100
        
        hbox:
            spacing 50
            label _("Enter или Пробел"):
                xsize 400
                text_size 36
            text _("Прохождение диалогов"):
                size 30
        
        hbox:
            spacing 50
            label "S":
                xsize 400
                text_size 36
            text _("Открывает настройки"):
                size 30
        
        hbox:
            spacing 50
            label "H":
                xsize 400
                text_size 36
            text _("Открывает историю"):
                size 30
        
        hbox:
            spacing 50
            label "V":
                xsize 400
                text_size 36
            text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}."):
                size 30
        
        hbox:
            spacing 50
            label "Ctrl + S":
                xsize 400
                text_size 36
            text _("Сохранение"):
                size 30

screen mouse_help():
    vbox:
        spacing 30
        xoffset 100
        
        hbox:
            spacing 50
            label _("Клик колёсиком"):
                xsize 400
                text_size 36
            text _("Скрывает интерфейс пользователя."):
                size 30

screen gamepad_help():
    vbox:
        spacing 30
        xoffset 100
        
        hbox:
            spacing 50
            label _("Правый триггер\nA/Нижняя кнопка"):
                xsize 400
                text_size 36
            text _("Прохождение диалогов, активация интерфейса."):
                size 30
        
        hbox:
            spacing 50
            label _("Левый Триггер\nЛевый Бампер"):
                xsize 400
                text_size 36
            text _("Откат назад по сюжету игры."):
                size 30
        
        hbox:
            spacing 50
            label _("Правый бампер"):
                xsize 400
                text_size 36
            text _("Откатывает предыдущее действие вперёд."):
                size 30
        
        hbox:
            spacing 50
            label _("Крестовина, Стики"):
                xsize 400
                text_size 36
            text _("Навигация по интерфейсу."):
                size 30
        
        hbox:
            spacing 50
            label _("Старт, Гид, B/Правая кнопка"):
                xsize 400
                text_size 36
            text _("Вход в игровое меню."):
                size 30
        
        hbox:
            spacing 50
            label _("Y/Верхняя кнопка"):
                xsize 400
                text_size 36
            text _("Скрывает интерфейс пользователя."):
                size 30
        
        hbox:
            spacing 50
            textbutton _("Калибровка") action GamepadCalibrate():
                xsize 400
                text_size 36