################################################################################
## Экран выбора
################################################################################

screen choice(items):
    style_prefix "choice"
    vbox:
        for i in items:
            textbutton i.caption action i.action