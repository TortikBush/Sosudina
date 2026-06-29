################################################################################
## Экран подтверждения
################################################################################

screen confirm(message, yes_action, no_action):
    modal True
    zorder 200
    style_prefix "confirm"
    add "gui/overlay/confirm.png"

    frame:
        vbox:
            xalign .5
            yalign .5
            spacing 90

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 300

                textbutton _("Да"):
                    action yes_action 
                    default True
                    keyboard_focus True
                textbutton _("Нет"):
                    action no_action

    key "game_menu" action no_action