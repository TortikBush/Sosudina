################################################################################
## Экран аккаунта
################################################################################

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
            action Show("account_ten_menu")
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
                
            action Show("account_boby_menu")
            
            focus_mask True
        
        imagebutton:
            idle "images/Dyx.png"
            hover "images/Dyx01.png"
            pos (1305, 1305)
            anchor (0.5, 0.5)
            at transform:
                zoom 1.9
            action Show("account_dyx_menu")
            focus_mask True
        
        imagebutton:
            idle "images/Provodnic.png"
            hover "images/Provodnic01.png"
            pos (1300, 705)
            anchor (0.5, 0.5)
            at transform:
                zoom 1.6
            action Show("account_provodnic_menu")
            focus_mask True

        textbutton "Выйти из аккаунта":
            text_size 40
            action Return()