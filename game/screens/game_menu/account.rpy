################################################################################
## Экран аккаунта
################################################################################
default name_edit_account = False
default player_name_input = ""


transform blink_cursor:

    alpha 1.0
    pause 0.5

    alpha 0.0
    pause 0.5

    repeat

init python:

    def get_player_name_width():

        if not persistent.player_name:
            return 0

        return len(persistent.player_name) * 40 + 15


screen account():
    tag menu
    add "images/account_bg.png"
    
    frame:
        background None
        xfill True
        yfill True
        
       
        if renpy.get_screen("account"):
            add "images/light.png" at transform:
                pos (1, 1.2)
                anchor (0, 1.0)
                zoom 1
                xzoom 0.9
                yzoom 0.7
                alpha 0.0
                pause 2
                linear 1.0 alpha 4
   
            
        imagebutton:
            idle "images/teny_account.png"
            hover "images/redy_teny.png"
            pos (570, 1250)
            anchor (0.5, 0.5)
            at transform:
                zoom 0.495
            action Show("ten_menu", origin="account")
            focus_mask True
            
        
        add "images/static_activ_account.png" at transform:
            pos (1300, 1221)  
            anchor (0.5, 0.5)
            zoom 0.885
            alpha 0.0
            pause 0.5
            linear 1.0 alpha 1.0

        add "images/boddy_for_account.png" at transform:
            pos (1300, 1221)  
            anchor (0.5, 0.5)
            zoom 0.885
            alpha 0.0
            pause 0.5
            linear 1.0 alpha 1.0

        imagebutton:
            idle "images/boddy_account.png"
            hover "images/boddy_account2.png"
            pos (1305, 1190)
            anchor (0.5, 0.5)
            at transform:
                zoom 0.495
            action Show("boby_menu", origin="account")
            
            focus_mask True
        
        imagebutton:
            idle "images/Dyx.png"
            hover "images/Dyx01.png"
            pos (1305, 1305)
            anchor (0.5, 0.5)
            at transform:
                zoom 1.9
            action Show("dyx_menu", origin="account")
            focus_mask True
        
        imagebutton:
            idle "images/Provodnic.png"
            hover "images/Provodnic01.png"
            pos (1300, 705)
            anchor (0.5, 0.5)
            at transform:
                zoom 1.6
            action Show("provodnic_menu", origin="account")
            focus_mask True
                
         
        vbox:
            xpos 3150
            ypos 726
            spacing 30
            
            

            
        #   дата и время
            text get_first_launch_date():
                size 60 
                color "#0a7a72"
                font "fronts/candara bold.ttf"
            
            null height 100

        vbox:
            xpos 2700
            ypos 405
            spacing 30
            # id
            text persistent.account_id:
                size 60
                font "fronts/candara bold.ttf"
                # color"#ffd700"
                
                color "#0a7a72"


            
            
            
        #   дата и время
        text "0/4":
                xpos 3100
                ypos 1495
               
                size 130
                font "fronts/NEOTHIC1.ttf"
                color "#c94848"
            
        
        
        fixed:
            xpos 2600
            ypos 90

            frame:
                background None
                xsize 700
                ysize 90


            if name_edit_account:

                input:
                    xpos -2000
                    ypos -2000
                    value FieldInputValue(persistent, "player_name")
                    length 20


                text persistent.player_name:
                    xpos 350
                    ypos 1
                    xanchor 0.5

                    font "fronts/Neothic.ttf"
                    size 120
                    color "#f8dd83"




                text "│":
                    xpos 350 + get_player_name_width() 
                    ypos 1
                   
                    font "DejaVuSans.ttf"
                    size 90
                    color "#f8dd83"

                    at blink_cursor   

                textbutton "Готово":
                    xoffset 290
                    yoffset 150
                    text_size 50

                    action [
                        SetVariable("name_edit_account", False),
                        Function(renpy.save_persistent)
                    ]

            else:


                if persistent.player_name == "":

                    text "Имя игрока":

                        xpos 350
                        ypos 1
                        xanchor 0.5

                        font "fronts/Neothic.ttf"
                        size 120
                        color "#888888"


                else:

                    text persistent.player_name:

                        xpos 350
                        ypos 1
                        xanchor 0.5

                        font "fronts/Neothic.ttf"
                        size 120
                        color "#f8dd83"



                textbutton "Изменить":

                    xoffset 230
                    yoffset 150

                    text_size 50
                    
                    action SetVariable("name_edit_account", True)

        vbox:
            xpos 2480
            ypos 1045
            spacing 20
          
            
            
            # Кнопки с цветами и размерами
            hbox:
                xalign 0.5
                spacing 50
                
                # Ламия (красная)
                button:
                    xsize 250
                    ysize 300
                    xoffset -80 
                    background None
                    hover_background None
                    action Show("in_development", character_name="Ламия")
              
                # Пифон (фиолетовая)
                button:
                    xsize 250
                    ysize 300
                    xoffset -30
                    background None
                    hover_background None
                    action Show("in_development", character_name="Пифон", origin="account")

                    
               
                
                # Ехидна (зелёная)
                button:
                    xsize 250
                    ysize 300
                    background None
                    hover_background None
                    action Show("in_development", character_name="Ехидна")
                    
                    
            
            null height 30
            
          
   

        textbutton "Выйти из аккаунта":
            text_size 40
            action Return()
        
            