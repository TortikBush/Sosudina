################################################################################
## Экран Об игре
################################################################################

screen about():
    tag menu
    use game_menu(_("Об игре"), scroll="viewport"):
        vbox:
            xoffset 700
            label "[config.name!t]"
            text _("Версия [config.version!t]\n")
            if gui.about:
                text "[gui.about!t]\n"
            text _("Сделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text