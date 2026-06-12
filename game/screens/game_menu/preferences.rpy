################################################################################
## Экран настроек
################################################################################


screen preferences():
    tag menu
    use game_menu(_("Настройки"), scroll="viewport"):
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
                    action [SetVariable("pref_tab", "screen"), ShowMenu("preferences")]
                    
                    if pref_tab == "screen":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Экран"):
                            style "tab_button_text_active"
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Экран"):
                            style "tab_button_text"
                
                button:
                    style "tab_button"
                    action [SetVariable("pref_tab", "text"), ShowMenu("preferences")]
                    
                    if pref_tab == "text":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Текст"):
                            style "tab_button_text_active"
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Текст"):
                            style "tab_button_text"
                
                button:
                    style "tab_button"
                    action [SetVariable("pref_tab", "audio"), ShowMenu("preferences")]
                    
                    if pref_tab == "audio":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Звук"):
                            style "tab_button_text_active"
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Звук"):
                            style "tab_button_text"
                
                button:
                    style "tab_button"
                    action [SetVariable("pref_tab", "skip"), ShowMenu("preferences")]
                    
                    if pref_tab == "skip":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Пропуск"):
                            style "tab_button_text_active"
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Пропуск"):
                            style "tab_button_text"

            fixed:
                xsize 1800
                ysize 800
                xalign 0.0
                yalign 0.5
                
                if pref_tab == "screen":
                    use pref_screen()
                elif pref_tab == "text":
                    use pref_text()
                elif pref_tab == "audio":
                    use pref_audio()
                elif pref_tab == "skip":
                    use pref_skip()
                else:
                    use pref_screen()

screen pref_screen():
    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.pref_spacing
        
        label _("Режим экрана:"):
            xalign 0.5
        
        hbox:
            xalign 0.5
            spacing gui.pref_spacing
            
            if renpy.variant("pc") or renpy.variant("web"):
                textbutton _("Оконный"):
                    action Preference("display", "window")
                    style "radio_button"
                    
                textbutton _("Полный"):
                    action Preference("display", "fullscreen")
                    style "radio_button"

screen pref_text():
    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.pref_spacing * 2
        xminimum 800
        
        vbox:
            xalign 0.5
            spacing gui.pref_spacing
            hbox:
                xalign 0.5
                spacing 30
                label _("Автовоспроизведение"):
                    yalign 0.5
                
                imagebutton:
                    idle Transform("gui/button/Galka_no_on.png", size=(70, 70))
                    hover Transform("gui/button/Galka_no_on.png", size=(70, 70))
                    selected_idle Transform("gui/button/Galka_on.png", size=(70, 70))
                    selected_hover Transform("gui/button/Galka_on.png", size=(70, 70))
                    action Preference("auto-forward", "toggle")
                    yoffset 4
        
        vbox:
            xalign 0.5
            spacing gui.pref_spacing
            label _("Скорость текста"):
                xalign 0.5
            bar:
                value Preference("text speed")
                xsize 600
                xalign 0.5
                style "pref_slider"
        
        vbox:
            xalign 0.5
            spacing gui.pref_spacing
            label _("Скорость авточтения"):
                xalign 0.5
            bar:
                value Preference("auto-forward time")
                xsize 600
                xalign 0.5
                style "pref_slider"
        
        text "Скорость авточтения работает только когда функция включена":
            xalign 0.5
            size 18
            color "#888888"

screen pref_audio():
    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.pref_spacing * 2
        xminimum 800

        vbox:
            xalign 0.5
            spacing 5
            imagebutton:
                idle Transform("sound.png", size=(90, 90))
                hover Transform("sound.png", size=(90, 90))
                selected_idle Transform("sound_off.png", size=(90, 90))
                selected_hover Transform("sound_off.png", size=(90, 90))
                action Preference("all mute", "toggle")
                selected Preference("all mute")

        vbox:
            xalign 0.5
            spacing gui.pref_spacing * 2

            if config.has_music:
                vbox:
                    xalign 0.5
                    spacing gui.pref_spacing
                    label _("Громкость музыки"):
                        xalign 0.5
                    hbox:
                        xalign 0.5
                        spacing gui.pref_spacing
                        bar:
                            value Preference("music volume")
                            xsize 600
                            style "pref_slider"

            if config.has_sound:
                vbox:
                    xalign 0.5
                    spacing gui.pref_spacing
                    label _("Громкость звуков"):
                        xalign 0.5
                    hbox:
                        xalign 0.5
                        spacing gui.pref_spacing
                        bar:
                            value Preference("sound volume")
                            xsize 600
                            style "pref_slider"
                        if config.sample_sound:
                            textbutton _("Тест"):
                                action Play("sound", config.sample_sound)
                                style "pref_slider_button"

            if config.has_voice:
                vbox:
                    xalign 0.5
                    spacing gui.pref_spacing
                    label _("Громкость голоса"):
                        xalign 0.5
                    hbox:
                        xalign 0.5
                        spacing gui.pref_spacing
                        bar:
                            value Preference("voice volume")
                            xsize 600
                            style "pref_slider"
                        if config.sample_voice:
                            textbutton _("Тест"):
                                action Play("voice", config.sample_voice)
                                style "pref_slider_button"

screen pref_skip():
    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.pref_spacing
        
        label _("Настройки пропуска"):
            xalign 0.5
        
        vbox:
            xalign 0.5
            spacing gui.pref_spacing
            textbutton _("Всего текста"):
                action Preference("skip", "toggle")
                style "check_button"
            textbutton _("После выборов"):
                action Preference("after choices", "toggle")
                style "check_button"
            textbutton _("Переходов"):
                action InvertSelected(Preference("transitions", "toggle"))
                style "check_button"