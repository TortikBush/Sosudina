# game/screens/characters/character_select.rpy

screen character_select():
    modal True

    add "images/Bg_choise.png"
    
    $ hovered_character = GetHoveredCharacter()
    
    frame:
        background None
        xalign 0.5
        yalign 0.45
        
        vbox:
            spacing 2000
            
            hbox:
                xalign 0.5
                spacing 200
                
                # Ламия
                vbox:
                    spacing 20
                    imagebutton:
                        idle "lami"
                        hover "lami"
                        hovered SetVariable("hovered_character", "Lami")
                        unhovered SetVariable("hovered_character", None)
                        action ShowMenu("in_development", character_name="Lami")
                    
                    fixed:
                        xsize 400
                        ysize 5
                        xalign 0.5
                        if hovered_character == "Lami":
                            add Solid("#ff8585", xsize=400, ysize=5):
                                xalign 0.5
                
                # Пифон
                vbox:
                    spacing 20
                    imagebutton:
                        idle "pifi"
                        hover "pifi"
                        hovered SetVariable("hovered_character", "Pifi")
                        unhovered SetVariable("hovered_character", None)
                        action [SetVariable("character_select", "pifi"), Show("pifon_stats")]
                    
                    fixed:
                        xsize 400
                        ysize 5
                        xalign 0.5
                        if hovered_character == "Pifi":
                            add Solid("#a974ff", xsize=400, ysize=5):
                                xalign 0.5
                
                # Ехидна
                vbox:
                    spacing 20
                    imagebutton:
                        idle "exi"
                        hover "exi"
                        hovered SetVariable("hovered_character", "Exi")
                        unhovered SetVariable("hovered_character", None)
                        action ShowMenu("in_development", character_name="Exi")
                    
                    fixed:
                        xsize 400
                        ysize 5
                        xalign 0.5
                        if hovered_character == "Exi":
                            add Solid("#9dfca2", xsize=400, ysize=5):
                                xalign 0.5

screen in_development(character_name):
    modal True
    
    frame:
        background "#00000080"  
        xfill True
        yfill True
        
        vbox:
            xalign 0.5
            yalign 0.3
            spacing 50
            xminimum 800
            
            text "Персонаж в разработке" size 85 color "#ff4f4f" xalign 0.5
            text "Нажмите чтобы закрыть" size 30 color "#CCCCCC" xalign 0.5
    
    key "dismiss" action Hide("in_development")
    key "mouseup_1" action Hide("in_development")

init python:
    if not hasattr(store, 'hovered_character'):
        hovered_character = None
    
    def GetHoveredCharacter():
        return store.hovered_character