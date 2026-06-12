###################################################################
# Общий шаблон для информационных экранов
###################################################################

transform fade_in_text:
    alpha 0.0
    pause 0.1
    linear 0.5 alpha 1.0

screen info_layout(title, text_content, screen_name):
    frame:
        xalign 0.5
        xoffset 800
        yalign 0.1
        background None
        vbox:
            xsize 1000
            text title:
                size 200
                color "#FFFFFF"
                outlines [(2, "#000000", 0, 0)]
                xalign 0.5
                at fade_in_text
            null height 10
            text text_content:
                size 30
                color "#FFFFFF"
                outlines [(1, "#000000", 0, 0)]
                line_spacing 5
                xalign 0.5
                at fade_in_text

    null height 200
    textbutton "← Назад":
        xpos 50
        ypos 50
        text_size 40
        text_color "#FFFFFF"
        text_hover_color "#FFAAAA"
        text_outlines [(2, "#000000", 0, 0)]
        action Hide(screen_name)