################################################################################
## Инициализация
################################################################################

init offset = -1
#######################################
################################################################################

################################################################################
## Стили
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## Внутриигровые экраны
################################################################################


## Экран разговора #############################################################
##
## Экран разговора используется для показа диалога игроку. Он использует два
## параметра — who и what — что, соответственно, имя говорящего персонажа и
## показываемый текст. (Параметр who может быть None, если имя не задано.)
##
## Этот экран должен создать текст с id "what", чтобы Ren'Py могла показать
## текст. Здесь также можно создать наложения с id "who" и id "window", чтобы
## применить к ним настройки стиля.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Если есть боковое изображение ("голова"), показывает её поверх текста.
    ## По стандарту не показывается на варианте для мобильных устройств — мало
    ## места.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Делает namebox доступным для стилизации через объект Character.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Экран ввода #################################################################
##
## Этот экран используется, чтобы показывать renpy.input. Это параметр запроса,
## используемый для того, чтобы дать игроку ввести в него текст.
##
## Этот экран должен создать наложение ввода с id "input", чтобы принять
## различные вводимые параметры.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Экран выбора ################################################################
##
## Этот экран используется, чтобы показывать внутриигровые выборы,
## представленные оператором menu. Один параметр, вложения, список объектов,
## каждый с заголовком и полями действия.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 810
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Экран быстрого меню #########################################################
##
## Быстрое меню показывается внутри игры, чтобы обеспечить лёгкий доступ к
## внеигровым меню.
default quick_menu_open = False
init python:
    def safe_rollback():
        if renpy.can_rollback():
            renpy.rollback()
        

screen quick_menu():
    zorder 100

    default menu_items = [
        ("Главное меню", ShowMenu('main_menu'), None),
        ("История", ShowMenu('history'), None),
        ("Пропуск", Skip(), Skip(fast=True, confirm=True)),
        ("Сохранения", ShowMenu('save'), None),
        ("Настройки", ShowMenu('preferences'), None),
        ("Помощь", ShowMenu('help'), None),
        
    ]
   
    # 🔹 КНОПКА НАЗАД
    imagebutton:
        align (0.0, 0.0)
        xoffset 40
        yoffset 50
        
    
        idle "images/arrow.png"
        hover "images/arrow.png" 
        action Function(safe_rollback)

    # 🔹 КНОПКА ☰ (исчезает при открытии)
    if not quick_menu_open:

        textbutton "☰" action SetVariable("quick_menu_open", True):
            align (1.0, 0.0)
            xoffset -120
            yoffset 50
            style "quick_button"
            xysize (120, 100)
            text_size 100

    # 🔹 САМО МЕНЮ (НЕ ВНУТРИ hbox!)
    if quick_menu_open:

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
                    action SetVariable("quick_menu_open", False)
                    xalign 0.5
                    text_size 60

## Данный код гарантирует, что экран быстрого меню будет показан в игре в любое
## время, если только игрок не скроет интерфейс.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Экраны Главного и Игрового меню
################################################################################

## Экран навигации #############################################################
##
## Этот экран включает в себя главное и игровое меню, и обеспечивает навигацию к
## другим меню и к началу игры.


default nav_buttons = [
   
    ("История", "history"),
    ("Аккаунт", "save_menu"),
    ("Настройки", "preferences"),
    ("Помощь", "help"),
    ("Об игре", "about"),
    ("Выход", None),
    
]
init python:
    nav_config = {
        "Начать игру": {
            "size": 135,
            "font": "fronts/Neothic.ttf",
            "offset": 0,
            "arrow": False
        },
        "История": {"offset": 600},
        "Аккаунт": {"offset": 615},
        "Настройки": {"offset": 515},
        "Помощь": {"offset": 610},
        "Об игре": {"offset": 630},
        "Выход": {"offset": 650,"arrow": True}, 
        "default": {
            "size": 90,
            "font": None,
            "offset": 600,
            "arrow": True
        }
    }
default hovered_button = None
screen navigation():
    
    add "images/Icon.png":
        xpos 110
        ypos 100
        zoom 0.7  

    add "images/line_mainmenu.png":
        xpos 2200
        ypos 1000
        zoom 0.7 
    textbutton "Начать игру":
        xpos 2300
        ypos 1100 # выбери нужную позицию
        text_size nav_config["Начать игру"]["size"]

        if nav_config["Начать игру"]["font"]:
            text_font nav_config["Начать игру"]["font"]

        action [SetVariable("hovered_button", None), ShowMenu("character_select")]

        hovered SetVariable("hovered_button", "Начать игру")
        unhovered SetVariable("hovered_button", None)
    vbox:
        style_prefix "navigation"
        xpos 3250
        yalign 0.93
        xanchor 1.0
        spacing gui.navigation_spacing

        for name, action_name in nav_buttons:
            
            $ base = nav_config["default"]
            $ custom = nav_config.get(name, {})
            $ cfg = dict(base, **custom)

            if name == "Выход":
                $ btn_action = Quit(confirm=False)  # Выход с подтверждением
            else:
                $ btn_action = [SetVariable("hovered_button", None), ShowMenu(action_name)]

            textbutton _(name):
                action btn_action

                text_size cfg["size"]

                if cfg["font"]:
                    text_font cfg["font"]

                

                # 👇 ВМЕСТО Show/Hide
                if cfg.get("arrow", True):  # arrow по умолчанию True
                    hovered SetVariable("hovered_button", name)
                    unhovered SetVariable("hovered_button", None)

    # ✅ стрелка теперь часть этого экрана
    if hovered_button:
        use arrow_screen(button_name=hovered_button)
                
    # 👇 стрелка теперь часть этого экрана
                
# Отдельный экран для стрелки
screen arrow_screen(button_name=""):
    # Определяем позицию для каждой кнопки с учетом их offset и yalign
    # порядок кнопок (как в nav_buttons, кроме первой)
    $ names = ["История", "Аккаунт", "Настройки", "Помощь", "Об игре","Выход"]

    if button_name in names:

        $ index = names.index(button_name)

        add "images/arrow.png":
            xpos 3350
            ypos 1300 + index * 130
            zoom 0.8
            at arrow_transform

transform arrow_transform:
    on show:
        alpha 0.0
        zoom 0.5
        linear 0.2 alpha 1.0 zoom 0.8
    on hide:
        linear 0.1 alpha 0.0

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")
    
###################################################################
# Экран таро
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
                    
                    # Подчеркивание по центру картинки Ламии
                    fixed:
                        xsize 400  # Ширина картинки Ламии
                        ysize 5
                        xalign 0.5  # Центрируем контейнер
                        if hovered_character == "Lami":
                            add Solid("#ff8585", xsize=400, ysize=5):  # Длина подчеркивания
                                xalign 0.5  # Центрируем само подчеркивание
                
                # Пифон
                vbox:
                    spacing 20
                    imagebutton:
                        idle "pifi"
                        hover "pifi"
                        hovered SetVariable("hovered_character", "Pifi")
                        unhovered SetVariable("hovered_character", None)
                        action [SetVariable("character_select", "pifi"), Show("pifon_stats")]
                    
                    # Подчеркивание по центру картинки Пифона
                    fixed:
                        xsize 400  # Ширина картинки Пифона
                        ysize 5
                        xalign 0.5  # Центрируем контейнер
                        if hovered_character == "Pifi":
                            add Solid("#a974ff", xsize=400, ysize=5):  # Длина подчеркивания
                                xalign 0.5  # Центрируем само подчеркивание
                
                # Ехидна
                vbox:
                    spacing 20
                    imagebutton:
                        idle "exi"
                        hover "exi"
                        hovered SetVariable("hovered_character", "Exi")
                        unhovered SetVariable("hovered_character", None)
                        action ShowMenu("in_development", character_name="Exi")
                    
                    # Подчеркивание по центру картинки Ехидны
                    fixed:
                        xsize 400  # Ширина картинки Ехидны
                        ysize 5
                        xalign 0.5  # Центрируем контейнер
                        if hovered_character == "Exi":
                            add Solid("#9dfca2", xsize=400, ysize=5):  # Длина подчеркивания
                                xalign 0.5  # Центрируем само подчеркивание
 
#Персонаж в разработке
screen in_development(character_name):
    modal True
    
    # Затемненный фон
    frame:
        background "#00000080"  
        xfill True
        yfill True
        
        vbox:
            xalign 0.5
            yalign 0.3
            spacing 50
            xminimum 800  # Минимальная ширина для центрирования
            
            text "Персонаж в разработке" size 85 color "#ff4f4f" xalign 0.5
            
            text "Нажмите чтобы закрыть" size 30 color "#CCCCCC" xalign 0.5
    
    # Закрытие по клику в любом месте
    key "dismiss" action Hide("in_development")
    key "mouseup_1" action Hide("in_development")

init python:
    if not hasattr(store, 'hovered_character'):
        hovered_character = None
    
    def GetHoveredCharacter():
        return store.hovered_character






# текст
# Пифи
transform fade_in(delay=0.0):
    alpha 0.0
    pause delay
    linear 0.5 alpha 1.0

screen pifon_stats():
    modal True
    
    # фон
    add "images/Bg_choise.png"

    frame:
        xalign 0.5
        xoffset 800
        yalign 0.1
        background None

        vbox:
            xsize 1000
            spacing 10

            text "ПИФОН":
                size 200
                color "#FFFFFF"
                outlines [(2, "#000000", 0, 0)]
                xalign 0.5
                at fade_in()

            text "особенность:":
                size 35
                color "#FFD700"
                outlines [(1, "#000000", 0, 0)]
                xalign 0.5
                at fade_in(0.5)

            text "Неконтролируемые видения прошлого и будущего":
                size 30
                color "#FFFFFF"
                outlines [(1, "#000000", 0, 0)]
                line_spacing 5
                xalign 0.5
                at fade_in(1.0)

            null height 200

            imagebutton:
                idle "images/knopka_vybrat.png"
                xalign 0.5
                action Start()

                

    # Подсветка
    if renpy.get_screen("pifon_stats"):
        add "images/light.png" at transform:
            # Позиция слева, не доходя до края
            pos (150, 0.95)  # x=100 от левого края, y=чуть выше нижнего края (0.95 = 95% высоты)
            anchor (0, 1.0)  # якорь в левом нижнем углу
            
            # Сжатие по горизонтали и вертикали
            zoom 0.7  # общий размер
            xzoom 0.9  # сжатие по горизонтали
            yzoom 0.7  # сжатие по вертикали (чем меньше, тем сильнее сжатие)
            
            alpha 0.0
            pause 2  # задержка перед появлением
            linear 1.0 alpha 4  # плавное проявление



    # ТЕНЬ
    imagebutton:
        idle "ten01.png"
        hover "ten02.png" 
        pos (670, 1095)
        anchor (0.5, 0.5)
        action Show("ten_menu")  

    # Пифи + подложка
    add "images/static_activ.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 0.0
        pause 0.5
        linear 1.0 alpha 1.0

    add "images/static.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 0.0
        pause 0.5
        linear 1.0 alpha 1.0

    # ТЕЛО
    imagebutton:
        idle "boby.png"
        hover "boby01.png"
        pos (1104, 1080)
        anchor (0.5, 0.5)
        focus_mask True 
        action Show("boby_menu")  

    # ПРОВОДНИК
    imagebutton:
        idle "Provodnic.png"
        hover "Provodnic01.png"
        pos (1104, 400)
        anchor (0.5, 0.5)
        action Show("provodnic_menu") 


    # ДУХ
    imagebutton:
        idle "Dyx.png"
        hover "Dyx01.png"
        pos (1104, 705)
        anchor (0.5, 0.5)
        focus_mask True 
        action Show("dyx_menu")  



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

            # Заголовок
            text title:
                size 200
                color "#FFFFFF"
                outlines [(2, "#000000", 0, 0)]
                xalign 0.5
                at fade_in_text

            null height 10

            # Основной текст
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

    # ТЕНЬ МЕНЮ
screen ten_menu():
    modal True

    add "images/Bg_choise.png"

    add "images/light.png" at transform:
            # Позиция слева, не доходя до края
            pos (850, 0.95)  # x=100 от левого края, y=чуть выше нижнего края (0.95 = 95% высоты)
            anchor (0, 1.0)  # якорь в левом нижнем углу
            
            # Сжатие по горизонтали и вертикали
            zoom 0.7  # общий размер
            xzoom 0.7  # сжатие по горизонтали
            yzoom 0.7  # сжатие по вертикали (чем меньше, тем сильнее сжатие)
            
            alpha 0.0
            pause 0.1 # задержка перед появлением
            linear 1.0 alpha 4  # плавное проявление


    add "images/ten01.png" at transform:
        pos (670, 1095)
        anchor (0.5, 0.5)
    add "images/ten02.png" at transform:
        pos (670, 1095)
        anchor (0.5, 0.5)
    add "images/static_activ.png" at transform:
        pos (1100, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
    add "images/static.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 1
        linear 1 alpha 0


    use info_layout(
        "ТЕНЬ",
        "это наше подсознание, оно формируется из опыта, который мы не можем или не хотим осознавать. Каждый прожитый день, каждое пережитое событие оставляет свой след, формируя нашу личность. Но не все воспоминания хранятся на поверхности сознания. Многие из них, особенно те, что связаны с негативными эмоциями, уходят в тень, в глубины подсознания. Они не исчезают бесследно, а продолжают влиять на наше поведение, формируя наши страхи, комплексы и предубеждения.Однако, тень – это не только хранилище негативных воспоминаний и подавленных желаний. В ней также могут скрываться наши таланты и способности, которые мы не решаемся проявить.Тень единственная составляющая личности которая может отделяться от тела по своему желанию.Отделившись от своего тела, Тень обретает самостоятельное существование, но платит за это высокую цену. Она лишается духовной силы, надежной защиты тела и мудрого руководства проводника, что делало ее прежнее существование столь безопасным.Однако, в редчайших случаях, при разрыве связи Тень может забрать с собой и дух.Это меняет ситуацию. Дух, освобожденный от оков физической оболочки, наделяет Тень невиданными прежде способностями, недоступными целостному существу.Ранее скрытые потенциалы высвобождаются, открывая новые горизонты возможностей.Но, несмотря на обретенную мощь, Тень остается уязвимой. Она лишена физической защиты, и ее существование висит на волоске. В любой момент она может бесследно исчезнуть в мрачных глубинах Леса, растворившись в его недрах навсегда.Свобода оборачивается вечным риском",
        "ten_menu"
    )


    # ТЕЛО МЕНЮ
screen boby_menu():
    modal True

    add "images/Bg_choise.png"

    add "images/boby02.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 1
        linear 0 alpha 1

    add "images/static.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 1
        linear 1 alpha 0

    use info_layout(
        "ТЕЛО",
        "Тело – это сосуд, сотканный из плоти, металла или иной материи.Он является вместилищем, в котором объединяются и взаимодействуют остальные компоненты,создавая тем самым жизнь.Тело как якорь, привязывает нас к реальности и оберегающий от растворения в лесной чаще забвения.",
        "boby_menu"
    )

# ДУХ МЕНЮ
screen dyx_menu():
    modal True

    add "images/Bg_choise.png"

    add "images/light.png" at transform:
            # Позиция слева, не доходя до края
            pos (690, 0.949)  # x=100 от левого края, y=чуть выше нижнего края (0.95 = 95% высоты)
            anchor (0, 1.0)  # якорь в левом нижнем углу
            
            # Сжатие по горизонтали и вертикали
            zoom 0.7  # общий размер
            xzoom 0.9  # сжатие по горизонтали
            yzoom 0.9  # сжатие по вертикали (чем меньше, тем сильнее сжатие)
            
            alpha 0.0
            pause 0.1 # задержка перед появлением
            linear 1.0 alpha 4  # плавное проявление


    add "images/static_activ.png" at transform:
        pos (1100, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485

    add "images/static.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 1
        linear 1 alpha 0

    add "images/Dyx02.png" at transform:
        pos (1101, 1050)  
        anchor (0.5, 0.5)
        zoom 0.5


    use info_layout(
        "ДУХ",
        "Дух - жизненная сила, топливо живого существа.После смерти, когда тело становится лишь пустой оболочкой, дух покидает его, отправляясь в странствие по Лесу в виде бесформенного эфира. Девять дней он скитается, прежде чем вернуться к могиле, где лежит тело (Либо же к месту смерти). Но это не конец, а лишь трансформация. Дух неисчезает бесследно, он находит новый дом – в скульптуре, или другом предмете.Эти артефакты, вместилища душ, называют болтунами. Они хранят в себе эхо прошлой жизни, отголоски мыслей, чувств и умений. Чем сильнее был человек при жизни,тем мощнее его дух.Апетханты - те же болтуны.Рядовые апетханты несут в себе силу Героев – мертвых мастеров своего дела, ремесленников, воинов, ученых. Эти апетханты обладают лишь навыками, отточенными при жизни.Более продвинутые апетханты содержат в себе дух Полубогов – святых, павших в войнемежду богами. Эти существа, некогда жившие ради высших идеалов, теперь служат своим новым хозяевам.Они понимают речь, могут выполнять команды, становясь верными союзниками Но самые редкие и могущественные апетханты – те, что созданы Мийосом, богом - кузнецом.Он создал четыре апетханта Эвриалу, Сфену, Медузу и Фемиду.А такжете которые сдержат дух самих богов (Пифон, Ламия, Ехидна, Цербер и Харибда).Такие апетханты уже имеют личность и характер В Пифоне находиться дух Севдоса (Снотворца)Из-за чего он и видит видения, однако из-за неимения других составляющих Севдоса (Тени и проводника) он не может их контролировать",
        "dyx_menu"
    )


# ПРОВОДНИК МЕНЮ
screen provodnic_menu():
    modal True

    add "images/Bg_choise.png"

    add "images/light.png" at transform:
            # Позиция слева, не доходя до края
            pos (690, 0.949)  # x=100 от левого края, y=чуть выше нижнего края (0.95 = 95% высоты)
            anchor (0, 1.0)  # якорь в левом нижнем углу
            
            # Сжатие по горизонтали и вертикали
            zoom 0.7  # общий размер
            xzoom 0.9  # сжатие по горизонтали
            yzoom 0.9  # сжатие по вертикали (чем меньше, тем сильнее сжатие)
            
            alpha 0.0
            pause 0.1 # задержка перед появлением
            linear 1.0 alpha 4  # плавное проявление


    add "images/static_activ.png" at transform:
        pos (1100, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485

    add "images/static.png" at transform:
        pos (1104, 1091)  
        anchor (0.5, 0.5)
        zoom 0.485
        alpha 1
        linear 1 alpha 0

    add "images/provodnic02.png" at transform:
        pos (1101, 700)  
        anchor (0.5, 0.5)
        zoom 0.5


    frame:
        xalign 0.5  
        xoffset 800  
        yalign 0.1
        background None
        
    use info_layout(
        "ПРОВОДНИК",
        "Проводник – это наш внутренний наставник, определяющий принципы и направляющий жизненный путь. Многие считают его голосом Леса, шепотом мудрости, пронизывающим сознание. Принципы, которые диктует проводник, не всегда просты и очевидны. Они могут ротиворечить общепринятым нормам и ожиданиям, но всегда направлены на сохранение внутренней целостности и гармонии с миром. Проводник – это не просто голос совести, это гораздо больше. Это внутренний камертон,настраивающий душу на правильную волну. Он помогает отличать истинное от ложного,важное от второстепенного, добро от зла.Смерть тела не означает исчезновения проводника. Он, освободившись от оков плоти,продолжает свое существование в других телах, вселяясь в животных и птиц.Такие животные и птицы имеют человеческие лица и являются священными",

        "provodnic_menu"
    )


## Экран главного меню #########################################################
##
## Используется, чтобы показать главное меню после запуска игры.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu


screen main_menu():

    ## Этот тег гарантирует, что любой другой экран с тем же тегом будет
    ## заменять этот.
    tag menu

    add gui.main_menu_background


    ## Эта пустая рамка затеняет главное меню.
    frame:
        style "main_menu_frame"

    ## Оператор use включает отображение другого экрана в данном. Актуальное
    ## содержание главного меню находится на экране навигации.
    use navigation


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 840
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -60
    xmaximum 2400
    yalign 1.0
    yoffset -60

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Экран игрового меню #########################################################
##
## Всё это показывает основную, обобщённую структуру экрана игрового меню. Он
## вызывается с экраном заголовка и показывает фон, заголовок и навигацию.
##
## Параметр scroll может быть None или один из "viewport" или "vpgrid". Этот
## экран предназначен для использования с одним или несколькими дочерними
## элементами, которые трансклюдируются (помещаются) внутрь него.

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

    style_prefix "game_menu"
    
    # Добавляем модальность и повышенный zorder
    modal True
    zorder 100

    if main_menu:
        add gui.main_menu_background
    else:
        add gui.game_menu_background

    frame:
        style "game_menu_outer_frame"

        hbox:
            ## Резервирует пространство для навигации.
            frame:
                style "game_menu_navigation_frame"

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":

                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        vbox:
                            spacing spacing

                            transclude

                elif scroll == "vpgrid":

                    vpgrid:
                        cols 1
                        yinitial yinitial

                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True

                        side_yfill True

                        spacing spacing

                        transclude

                else:

                    transclude

    textbutton _("Вернуться"):
        style "return_button"

        action Return()

    label title
    


style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_viewport is gui_viewport
style game_menu_side is gui_side
style game_menu_scrollbar is gui_vscrollbar

style game_menu_label is gui_label
style game_menu_label_text is gui_label_text

style return_button is navigation_button
style return_button_text is navigation_button_text

style game_menu_outer_frame:
    bottom_padding 90
    top_padding 240  # Изменено с 360 на 280 для поднятия содержимого выше
    background "gui/overlay/game_menu.png"

style game_menu_navigation_frame:
    xsize 10
    ysize 10


style game_menu_content_frame:
    left_margin 1
    right_margin 60
    top_margin 10  # Изменено с 30 на 20 для дополнительного поднятия

style game_menu_viewport:
    xsize 2760

style game_menu_vscrollbar:
    unscrollable gui.unscrollable

style game_menu_side:
    spacing 30

style game_menu_label:
    xpos 150
    ysize 100

style game_menu_label_text:
    size 60
    color gui.accent_color
    ypos 70  # Изменено с 70 на 50 для поднятия заголовка выше

style return_button:
    xpos 3300
    ypos 50

## Экран Об игре ###############################################################
##
## Этот экран показывает авторскую информацию об игре и Ren'Py.
##
## В этом экране нет ничего особенного, и он служит только примером того, каким
## можно сделать свой экран.

screen about():

    tag menu

    ## Этот оператор включает игровое меню внутрь этого экрана. Дочерний vbox
    ## включён в порт просмотра внутри экрана игрового меню.
    use game_menu(_("Об игре"), scroll="viewport"):

        vbox:
            
            xoffset 700

            label "[config.name!t]"
            text _("Версия [config.version!t]\n")

            ## gui.about обычно установлено в options.rpy.
            if gui.about:
                text "[gui.about!t]\n"
                

            text _("Сделано с помощью {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")


style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style game_menu_label_text:
    xoffset 20

## Экран сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

screen save_menu():

    tag menu

    use file_slots(_("Сохранения"))


## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

screen save():

    tag menu

    use file_slots(_("Сохранения"))


## Экраны загрузки и сохранения ################################################
##
## Эти экраны ответственны за возможность сохранять и загружать игру. Так
## как они почти одинаковые, оба реализованы по правилам третьего экрана —
## file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save 

screen file_slots(title, mode="save"):

    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"))
    
    # Определяем, находимся ли мы на странице автосохранений
    $ is_auto_page = FileCurrentPage() == "auto"
    
    # Определяем количество страниц на основе заполненных слотов
    $ total_pages = 1
    if renpy.get_screen("save") or renpy.get_screen("load"):
        for page in range(1, 100):  # Проверяем до 100 страниц
            $ page_has_saves = False
            for slot in range(1, gui.file_slot_cols * gui.file_slot_rows + 1):
                if FileLoadable(slot, page=page):
                    $ page_has_saves = True
                    break
            if page_has_saves:
                $ total_pages = page
            else:
                # Если нашли пустую страницу после непустой, останавливаемся
                if page > total_pages:
                    break
        
        # Добавляем еще одну пустую страницу для новых сохранений
        $ total_pages += 1

    use game_menu(title):

        fixed:
            order_reverse True

            # Сортировка сохранений по главам (страницам)
            # Создаем список страниц с информацией о главах
            $ chapters = []
            for page_num in range(1, total_pages + 1):
                $ chapter_name = "Глава {}".format(page_num)
                $ chapter_has_saves = False
                $ chapter_saves = []
                
                for slot in range(1, gui.file_slot_cols * gui.file_slot_rows + 1):
                    if FileLoadable(slot, page=page_num):
                        $ chapter_has_saves = True
                        $ chapter_saves.append(slot)
                
                # Получаем дополнительную информацию о сохранениях в главе
                if chapter_has_saves:
                    $ chapter_info = {
                        'number': page_num,
                        'name': chapter_name,
                        'has_saves': True,
                        'saves': chapter_saves,
                        'last_save_time': FileTime(chapter_saves[-1], page=page_num, format='%d.%m.%Y %H:%M') if chapter_saves else None
                    }
                else:
                    $ chapter_info = {
                        'number': page_num,
                        'name': chapter_name,
                        'has_saves': False,
                        'saves': [],
                        'last_save_time': None
                    }
                
                $ chapters.append(chapter_info)

            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"
                xalign 0.5
                yalign 0.5
                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):
                    $ slot = i + 1
                    
                    # Проверяем, есть ли сохранение в этом слоте
                    $ has_save = FileLoadable(slot)
                    
                    # Определяем действие для кнопки слота
                    $ slot_action = If(
                        mode == "save",
                        FileAction(slot),  # Для сохранения - запись
                        FileLoad(slot)     # Для загрузки - чтение
                    )
                    
                    # Получаем информацию о сохранении
                    $ save_time = FileTime(slot, format='%d.%m.%Y %H:%M') if has_save else None
                    $ save_date = FileTime(slot, format='%d.%m.%Y') if has_save else None
                    $ save_time_only = FileTime(slot, format='%H:%M') if has_save else None
                    
                    button:
                        style "slot_button"
                        action slot_action
                        xpadding 0
                        ypadding 0

                        has fixed:
                            fit_first True
                            xfit True
                            yfit True

                        # Иконка сохранения (скриншот)
                        add FileScreenshot(slot) 
                        xalign 0.5
                        yalign 0.17
                        
                        # Информация о сохранении
                        vbox:
                            xpos 0
                            ypos 420  # Располагаем под иконкой
                            
                            # Название сохранения (глава)
                            if has_save:
                                text FileSaveName(slot):
                                    style "slot_name_text"
                                    size 14
                            
                            # Дата и время сохранения
                            if has_save and save_date and save_time_only:
                                text save_date + " " + save_time_only:
                                    style "slot_date_text"
                                    size 30
                                    color "#ffd359"
                            
                        
                
                        if has_save:
                            # кнопки
                            fixed:
                                xalign 1.0
                                yalign 0.0
                                xoffset -20  # Отступ от правого края
                                
                                # Кнопка загрузки (стрелка вниз)
                                button:
                                    style "icon_button"
                                    action FileLoad(slot)
                                    tooltip "Загрузить это сохранение"
                                    xpos 785
                                    ypos -31
                                    
                                    text "▼" style "icon_text"
                                
                                # Кнопка удаления (крестик)
                                button:
                                    style "icon_button"
                                    action FileDelete(slot)
                                    tooltip "Удалить это сохранение"
                                    xpos 785
                                    ypos 55
                                    
                                    text "✕" style "icon_text"
                        
                        # Для пустых слотов в режиме сохранения показываем кнопку "СОХРАНИТЬ" 
                        elif mode == "save" and not is_auto_page:
                            vbox:
                                xalign 0.5
                                ypos 170
                                
                                textbutton _("СОХРАНИТЬ"):
                                    action FileAction(slot)
                                    style "save_under_button"
                                    text_style "save_under_text"

            # Панель навигации по страницам с подписями глав
            vbox:
                style_prefix "page"
                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5
                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}А") action FilePage("auto")

                    # Динамическое отображение страниц с подписями глав
                    for page_info in chapters:
                        $ page_num = page_info['number']
                        $ is_current = FileCurrentPage() == page_num
                        
                        # Создаем кнопку страницы с подписью главы
                        if is_current:
                            textbutton "[page_num]":
                                action FilePage(page_num)
                                style "page_num_current_button"
                                tooltip page_info['name']
                        else:
                            textbutton "[page_num]":
                                action FilePage(page_num)
                                style "page_num_button"
                                tooltip page_info['name']

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Загрузить на сервер"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Скачать сохранения с сервера"):
                            action DownloadSync()
                            xalign 0.5



style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 150
    ypadding 9
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")


## Экран настроек ##############################################################
##
## Экран настроек позволяет игроку настраивать игру под себя.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen preferences():

    tag menu

    use game_menu(_("Настройки"), scroll="viewport"):


        # Основной контейнер с горизонтальным расположением
        hbox:
            xalign 0.0
            yalign 0.4
            spacing 50
            
            # Левая панель с вертикальными вкладками
            vbox:
                xalign 0.0  
                xoffset 50  
                yalign 1  
                spacing 40  
                
                # Вкладка "Экран"
                button:
                    style "tab_button"
                    action [SetVariable("pref_tab", "screen"), ShowMenu("preferences")]
                    
                    if pref_tab == "screen":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Экран"):
                            style "tab_button_text_active"  # Активный стиль текста
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Экран"):
                            style "tab_button_text"  # Обычный стиль текста
                
                # Вкладка "Текст"
                button:
                    style "tab_button"
                    action [SetVariable("pref_tab", "text"), ShowMenu("preferences")]
                    
                    if pref_tab == "text":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Текст"):
                            style "tab_button_text_active"
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Текст"):
                            style "tab_button_text"
                      
        
                
                # Вкладка "Звук"
                button:
                    style "tab_button"
                    action [SetVariable("pref_tab", "audio"), ShowMenu("preferences")]
                    
                    if pref_tab == "audio":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Звук"):
                            style "tab_button_text_active"
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Звук"):
                            style "tab_button_text"
                
                # Вкладка "Пропуск"
                button:
                    style "tab_button"
                    action [SetVariable("pref_tab", "skip"), ShowMenu("preferences")]
                    
                    if pref_tab == "skip":
                        add Transform("gui/tab_active.png", size=(450, 180))
                        text _("Пропуск"):
                            style "tab_button_text_active"
                    else:
                        add Transform("gui/tab_idle.png", size=(450, 180))
                        text _("Пропуск"):
                            style "tab_button_text"

            # Правая панель с содержимым
            fixed:
                xsize 1800
                ysize 800
                xalign 0.0
                yalign 0.5
                
                # Показываем только одну вкладку в зависимости от переменной
                if pref_tab == "screen":
                    use pref_screen()
                elif pref_tab == "text":
                    use pref_text()
                elif pref_tab == "audio":
                    use pref_audio()
                elif pref_tab == "skip":
                    use pref_skip()
                else:
                    # По умолчанию показываем экран
                    use pref_screen()

screen pref_screen():
    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.pref_spacing
        
        label _("Режим экрана:"):
            xalign 0.5
        
        hbox:
            xalign 0.5
            spacing gui.pref_spacing
            
            if renpy.variant("pc") or renpy.variant("web"):
                textbutton _("Оконный"):
                    action Preference("display", "window")
                    style "radio_button"
                    
                textbutton _("Полный"):
                    action Preference("display", "fullscreen")
                    style "radio_button"

screen pref_text():
    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.pref_spacing * 2
        xminimum 800
        
        # Переключатель автовоспроизведения
        vbox:
            xalign 0.5
            spacing gui.pref_spacing

            hbox:
                xalign 0.5
                spacing 30
                label _("Автовоспроизведение"):
                    yalign 0.5
                
                imagebutton:
                    idle Transform("gui/button/Galka_no_on.png", size=(70, 70))
                    hover Transform("gui/button/Galka_no_on.png", size=(70, 70))
                    selected_idle Transform("gui/button/Galka_on.png", size=(70, 70))
                    selected_hover Transform("gui/button/Galka_on.png", size=(70, 70))
                    action Preference("auto-forward", "toggle")
                    yoffset 4
        # Скорость текста
        vbox:
            xalign 0.5
            spacing gui.pref_spacing
            
            label _("Скорость текста"):
                xalign 0.5
            
            bar:
                value Preference("text speed")
                xsize 600
                xalign 0.5
                style "pref_slider"
        
        # Скорость авточтения
        vbox:
            xalign 0.5
            spacing gui.pref_spacing
            
            label _("Скорость авточтения"):
                xalign 0.5
            
            bar:
                value Preference("auto-forward time")
                xsize 600
                xalign 0.5
                style "pref_slider"
        
        # Подсказка
        text "Скорость авточтения работает только когда функция включена":
            xalign 0.5
            size 18
            color "#888888"

screen pref_audio():
    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.pref_spacing * 2
        xminimum 800

        # Кнопка включения/выключения звука (по центру сверху)
        vbox:
            xalign 0.5
            spacing 5

            imagebutton:
                idle Transform("sound.png", size=(90, 90))
                hover Transform("sound.png", size=(90, 90))
                selected_idle Transform("sound_off.png", size=(90, 90))
                selected_hover Transform("sound_off.png", size=(90, 90))

                action Preference("all mute", "toggle")
                selected Preference("all mute")

        # Ползунки
        vbox:
            xalign 0.5
            spacing gui.pref_spacing * 2

            if config.has_music:
                vbox:
                    xalign 0.5
                    spacing gui.pref_spacing

                    label _("Громкость музыки"):
                        xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing gui.pref_spacing

                        bar:
                            value Preference("music volume")
                            xsize 600
                            style "pref_slider"

            if config.has_sound:
                vbox:
                    xalign 0.5
                    spacing gui.pref_spacing

                    label _("Громкость звуков"):
                        xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing gui.pref_spacing

                        bar:
                            value Preference("sound volume")
                            xsize 600
                            style "pref_slider"

                        if config.sample_sound:
                            textbutton _("Тест"):
                                action Play("sound", config.sample_sound)
                                style "pref_slider_button"

            if config.has_voice:
                vbox:
                    xalign 0.5
                    spacing gui.pref_spacing

                    label _("Громкость голоса"):
                        xalign 0.5

                    hbox:
                        xalign 0.5
                        spacing gui.pref_spacing

                        bar:
                            value Preference("voice volume")
                            xsize 600
                            style "pref_slider"

                        if config.sample_voice:
                            textbutton _("Тест"):
                                action Play("voice", config.sample_voice)
                                style "pref_slider_button"
                

screen pref_skip():
    vbox:
        xalign 0.5
        yalign 0.5
        spacing gui.pref_spacing
        
        label _("Настройки пропуска"):
            xalign 0.5
        
        vbox:
            xalign 0.5
            spacing gui.pref_spacing
            
            textbutton _("Всего текста"):
                action Preference("skip", "toggle")
                style "check_button"
            
            textbutton _("После выборов"):
                action Preference("after choices", "toggle")
                style "check_button"
            
            textbutton _("Переходов"):
                action InvertSelected(Preference("transitions", "toggle"))
                style "check_button"


default pref_tab = "screen"

# Единые стили для всех вкладок
style tab_button:
    xsize 450
    ysize 180
    padding (0, 0)
    
style tab_button_text:
    size 64
    color "#0a7a72"  # Бирюзовый цвет для неактивных вкладок
    xalign 0.5
    yalign 0.5
    
style tab_button_text_active:
    size 64
    color "#ffdd80"  # Золотистый цвет для активной вкладки
    xalign 0.5
    yalign 0.5

# Стили для остальных элементов
style pref_button_text is gui_button_text

style pref_slider:
    left_bar Transform("gui/slider/bar_full.png", size=(600, 70))
    right_bar Transform("gui/slider/bar_empty.png", size=(600, 70))
    thumb Transform("gui/slider/thumb.png", size=(20, 72))
    xalign 0.5
    yalign 1

style pref_slider_button:
    yalign 0.5
    left_margin 30

style mute_all_button:
    xalign 0.5
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style radio_button:
    xalign 0.5
    foreground "gui/button/radio_[prefix_]foreground.png"

style check_button:
    xalign 0.5
    foreground "gui/button/check_[prefix_]foreground.png"

## Экран истории ###############################################################
##
## Этот экран показывает игроку историю диалогов. Хотя в этом экране нет ничего
## особенного, он имеет доступ к истории диалогов, хранимом в _history_list.
##
## https://www.renpy.org/doc/html/history.html

screen history():

    tag menu

    ## Избегайте предсказывания этого экрана, так как он может быть очень
    ## массивным.
    predict False

    use game_menu(_("История"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

        style_prefix "history"

        for h in _history_list:

            window:

                ## Это всё правильно уравняет, если history_height будет
                ## установлен на None.
                has fixed:
                    yfit True

                if h.who:

                    label h.who:
                        style "history_name"
                        substitute False

                        ## Берёт цвет из who параметра персонажа, если он
                        ## установлен.
                        if "color" in h.who_args:
                            text_color h.who_args["color"]

                $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
                text what:
                    substitute False

        if not _history_list:
            label _("История диалогов пуста.")


## Это определяет, какие теги могут отображаться на экране истории.

define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


style history_window is empty

style history_name is gui_label
style history_name_text is gui_label_text
style history_text is gui_text

style history_label is gui_label
style history_label_text is gui_label_text

style history_window:
    xfill True
    ysize gui.history_height

style history_name:
    xpos gui.history_name_xpos
    xanchor gui.history_name_xalign
    ypos gui.history_name_ypos
    xsize gui.history_name_width

style history_name_text:
    min_width gui.history_name_width
    textalign gui.history_name_xalign

style history_text:
    xpos gui.history_text_xpos
    ypos gui.history_text_ypos
    xanchor gui.history_text_xalign
    xsize gui.history_text_width
    min_width gui.history_text_width
    textalign gui.history_text_xalign
    layout ("subtitle" if gui.history_text_xalign else "tex")

style history_label:
    xfill True

style history_label_text:
    xalign 0.5


## Экран помощи ################################################################
##
## Экран, дающий информацию о клавишах управления. Он использует другие экраны
## (keyboard_help, mouse_help, и gamepad_help), чтобы показывать актуальную
## помощь.

screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Помощь"), scroll="viewport"):

        style_prefix "help"

        vbox:
            spacing 45

            hbox:

                textbutton _("Клавиатура") action SetScreenVariable("device", "keyboard")
                textbutton _("Мышь") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Геймпад") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Enter или Пробел")
        text _("Прохождение диалогов")

    hbox:
        label "S"
        text _("Открывает настройки")

    hbox:
        label "H"
        text _("Открывает историю")

    hbox:
        label "V"
        text _("Включает поддерживаемый {a=https://www.renpy.org/l/voicing}синтезатор речи{/a}.")

    hbox:
        label "Cntrl + S"
        text _("Сохранение")


screen mouse_help():

    hbox:
        label _("Клик колёсиком")
        text _("Скрывает интерфейс пользователя.")


screen gamepad_help():

    hbox:
        label _("Правый триггер\nA/Нижняя кнопка")
        text _("Прохождение диалогов, активация интерфейса.")

    hbox:
        label _("Левый Триггер\nЛевый Бампер")
        text _("Откат назад по сюжету игры.")

    hbox:
        label _("Правый бампер")
        text _("Откатывает предыдущее действие вперёд.")

    hbox:
        label _("Крестовина, Стики")
        text _("Навигация по интерфейсу.")

    hbox:
        label _("Старт, Гид, B/Правая кнопка")
        text _("Вход в игровое меню.")

    hbox:
        label _("Y/Верхняя кнопка")
        text _("Скрывает интерфейс пользователя.")

    textbutton _("Калибровка") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 24

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 750
    right_padding 60

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0

    




################################################################################
## Дополнительные экраны
################################################################################


## Экран подтверждения #########################################################
##
## Экран подтверждения вызывается, когда Ren'Py хочет спросить у игрока вопрос
## Да или Нет.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Гарантирует, что другие экраны будут недоступны, пока показан этот экран.
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

                textbutton _("Да") action yes_action
                textbutton _("Нет") action no_action

    ## Правый клик и esc, как ответ "Нет".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Экран индикатора пропуска ###################################################
##
## Экран индикатора пропуска появляется для того, чтобы показать, что идёт
## пропуск.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 18

            text _("Пропускаю")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Эта трансформация используется, чтобы мигать стрелками одна за другой.
transform delayed_blink(delay, cycle):
    alpha .5

    pause delay

    block:
        linear .2 alpha 1.0
        pause .2
        linear .2 alpha 0.5
        pause (cycle - .4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Нам надо использовать шрифт, имеющий в себе символ U+25B8 (стрелку выше).
    font "DejaVuSans.ttf"


## Экран уведомлений ###########################################################
##
## Экран уведомлений используется, чтобы показать игроку оповещение. (Например,
## когда игра автосохранилась, или был сделан скриншот)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Экран NVL ###################################################################
##
## Этот экран используется в диалогах и меню режима NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Показывает диалог или в vpgrid, или в vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Показывает меню, если есть. Меню может показываться некорректно, если
        ## config.narrator_menu установлено на True.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Это контролирует максимальное число строк NVL, могущих показываться за раз.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Пузырьковый экран ###########################################################
##
## Экран пузырьков используется для отображения диалога игроку при использовании
## речевых пузырьков. Экран пузырьков принимает те же параметры, что и экран
## say, должен создать отображаемый объект с id "what", и может создавать
## отображаемые объекты с id "namebox", "who" и "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}

