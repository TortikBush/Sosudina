################################################################################
## Экран аккаунта
################################################################################
default name_edit_account = False
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
            xpos 3200
            ypos 650
            spacing 30
            
            
            
            text "Первый запуск:" size 40 color "#ffd700"
            text get_first_launch_date() size 40 color "#aaaaaa"
            
            null height 100

        vbox:
            xpos 2700
            ypos 350
            spacing 30

            text "ID аккаунта:":
                size 40
                color "#ffd700"

            text persistent.account_id:
                size 40
                color "#aaaaaa"
        
        fixed:
            xpos 2400
            ypos 150

            frame:
                background None
                xsize 700
                ysize 90


            if name_edit_account:

                input:
                    xpos 20
                    ypos 20
                    value FieldInputValue(persistent, "player_name")
                    length 20
                    pixel_width 500
                    size 40
                    color "#ffffff"


                textbutton "Готово":
                    xpos 560
                    ypos 10
                    text_size 35
                    action [
                        SetVariable("name_edit_account", False),
                        Function(renpy.save_persistent)
                    ]


            else:

                if persistent.player_name == "":
                    text "Имя игрока":
                        xpos 20
                        ypos 20
                        size 40
                        color "#888888"

                else:
                    text persistent.player_name:
                        xpos 20
                        ypos 20
                        size 40
                        color "#ffffff"


                textbutton "Изменить":
                    xpos 560
                    ypos 10
                    text_size 35
                    action SetVariable("name_edit_account", True)
            

        textbutton "Выйти из аккаунта":
            text_size 40
            action Return()
        
            