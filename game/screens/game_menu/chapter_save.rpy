# game/screens/game_menu/chapter_save.rpy

screen chapter_save():
    tag menu
    
    use game_menu(_("ПЕРЕЙТИ К")):
        
        fixed:
            xfill True
            yfill True
            
            viewport:
                id "chapters_viewport"
                xfill True
                ysize 320
                ypos 100
                draggable True
                mousewheel True
                
                hbox:
                    spacing 25
                    
                    for chapter_id, chapter in persistent.chapter_progress.items():
                        $ chapter_num = chapter_id.split("_")[1]
                        
                        frame:
                            xsize 340
                            ysize 280
                            background "#4a4a4a"
                            
                            if chapter["unlocked"]:
                                button:
                                    xfill True
                                    yfill True
                                    action Jump(chapter_id)
                                    
                                    vbox:
                                        xalign 0.5
                                        yalign 0.5
                                        spacing 10
                                        
                                        text "ГЛАВА {}".format(chapter_num):
                                            size 18
                                            color "#ffd700"
                                            xalign 0.5
                                        
                                        text chapter["name"]:
                                            size 24
                                            color "#ffffff"
                                            xalign 0.5
                                            textalign 0.5
                                        
                                        if chapter["completed"]:
                                            text "ПРОЙДЕНО" size 18 color "#00ff00" xalign 0.5
                                        else:
                                            text "ДОСТУПНО" size 18 color "#ffd700" xalign 0.5
                            else:
                                vbox:
                                    xalign 0.5
                                    yalign 0.5
                                    spacing 10
                                    
                                    text "ГЛАВА {}".format(chapter_num):
                                        size 18
                                        color "#555"
                                        xalign 0.5
                                    
                                    text chapter["name"]:
                                        size 24
                                        color "#555"
                                        xalign 0.5
                                        textalign 0.5
                                    
                                    text "ЗАБЛОКИРОВАНО" size 18 color "#555" xalign 0.5
            
            bar:
                value XScrollValue("chapters_viewport")
                xsize 1000
                ysize 20
                xalign 0.5
                yalign 0.95
                left_bar "#ffd700"
                right_bar "#333333"
                thumb "#ffffff"
            
            text "→  листайте вправо/влево  ←" size 18 color "#888888" xalign 0.5 ypos 720