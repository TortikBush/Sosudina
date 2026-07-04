################################################################################
## Экран быстрого меню
################################################################################

init python:

    if not hasattr(store, "quick_menu_open"):
        store.quick_menu_open = False

    def open_quick_menu():
        store.quick_menu_open = True
        renpy.restart_interaction()

    def close_quick_menu():
        store.quick_menu_open = False
        renpy.restart_interaction()

    def safe_rollback():
        store.quick_menu_open = False
        renpy.restart_interaction()

        if renpy.can_rollback():
            renpy.rollback()


init python:
    config.overlay_screens.append("quick_menu")


screen quick_menu():

    zorder 100

    if store.quick_menu_open:
        key "dismiss" action Function(close_quick_menu)

    default menu_items = [
        ("Главное меню", [Function(renpy.save, "autosave"), MainMenu()], None),
        ("История", ShowMenu("history"), None),
        ("Пропуск", Skip(), Skip(fast=True, confirm=True)),
        ("Сохранения", ShowMenu("save"), None),
        ("Настройки", ShowMenu("preferences"), None),
        ("Помощь", ShowMenu("help"), None),
    ]

    imagebutton:
        align (0.0, 0.0)
        xoffset 40
        yoffset 50
        idle "images/arrow.png"
        hover "images/arrow.png"
        action Function(safe_rollback)

    if not store.quick_menu_open:

        textbutton "☰":
            action Function(open_quick_menu)

            align (1.0, 0.0)
            xoffset -120
            yoffset 50
            style "quick_button"
            xysize (120, 100)
            text_size 100

    if store.quick_menu_open:

        frame:
            background Solid("#0a1a1b")
            padding (15, 10)
            xalign 1.0
            yalign 0.0
            xoffset -50
            yoffset 100
            xmaximum 10000
            ymaximum 1000

            vbox:
                spacing 8

                for item_label, item_action, item_alt in menu_items:

                    if item_alt:
                        textbutton _(item_label):
                            action item_action
                            alternate item_alt
                            text_size 55
                    else:
                        textbutton _(item_label):
                            action item_action
                            text_size 55

                null height 10

                textbutton "Закрыть":
                    action Function(close_quick_menu)
                    xalign 0.5
                    text_size 60