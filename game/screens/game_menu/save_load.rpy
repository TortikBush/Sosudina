################################################################################
## Экраны сохранения и загрузки
################################################################################

screen save_menu():
    tag menu
    use file_slots(_("Сохранения"))

# screen save():
#     tag menu
#     use file_slots(_("Сохранения"))

screen file_slots(title, mode="save"):
    default page_name_value = FilePageNameInputValue(pattern=_("{} страница"), auto=_("Автосохранения"))
    
    $ is_auto_page = FileCurrentPage() == "auto"
    
    $ total_pages = 1
    if renpy.get_screen("save") or renpy.get_screen("load"):
        for page in range(1, 10):
            $ page_has_saves = False
            for slot in range(1, gui.file_slot_cols * gui.file_slot_rows + 1):
                if FileLoadable(slot, page=page):
                    $ page_has_saves = True
                    break
            if page_has_saves:
                $ total_pages = page
            else:
                if page > total_pages:
                    break
        $ total_pages += 1

    use game_menu(title):
        fixed:
            order_reverse True

            $ chapters = []
            for page_num in range(1, total_pages + 1):
                $ chapter_name = "Глава {}".format(page_num)
                $ chapter_has_saves = False
                $ chapter_saves = []
                
                for slot in range(1, gui.file_slot_cols * gui.file_slot_rows + 1):
                    if FileLoadable(slot, page=page_num):
                        $ chapter_has_saves = True
                        $ chapter_saves.append(slot)
                
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
                    $ has_save = FileLoadable(slot)
                    
                    $ slot_action = If(
                        mode == "save",
                        FileAction(slot),
                        FileLoad(slot)
                    )
                    
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

                        add FileScreenshot(slot):
                            xalign 0.5
                            yalign 0.17
                        
                        vbox:
                            xpos 0
                            ypos 420
                            
                            if has_save:
                                text FileSaveName(slot):
                                    style "slot_name_text"
                                    size 14
                            
                            if has_save and save_date and save_time_only:
                                text save_date + " " + save_time_only:
                                    style "slot_date_text"
                                    size 30
                                    color "#ffd359"
                        
                        if has_save:
                            fixed:
                                xalign 1.0
                                yalign 0.0
                                xoffset -20
                                
                                button:
                                    style "icon_button"
                                    action FileLoad(slot)
                                    tooltip "Загрузить это сохранение"
                                    xpos 785
                                    ypos -31
                                    text "▼" style "icon_text"
                                
                                button:
                                    style "icon_button"
                                    action FileDelete(slot)
                                    tooltip "Удалить это сохранение"
                                    xpos 785
                                    ypos 55
                                    text "✕" style "icon_text"
                        
                        elif mode == "save" and not is_auto_page:
                            vbox:
                                xalign 0.5
                                ypos 170
                                textbutton _("СОХРАНИТЬ"):
                                    action FileAction(slot)
                                    style "save_under_button"
                                    text_style "save_under_text"
  
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
                        textbutton _("Авто") action FilePage("auto")

                    # Определяем, сколько слотов на странице
                    $ total_slots = gui.file_slot_cols * gui.file_slot_rows
                    $ current_page = FileCurrentPage()
                    
                    # Проверяем, полностью ли заполнена ТЕКУЩАЯ страница
                    $ current_page_full = True
                    python:
                        for slot in range(1, total_slots + 1):
                            if not FileLoadable(slot, page=current_page):
                                current_page_full = False
                                break
                    
                    # Показываем кнопки страниц (только реально существующие)
                    $ max_page = 1
                    python:
                        # Находим последнюю страницу с сохранениями
                        for page in range(1, 20):
                            page_has_saves = False
                            for slot in range(1, total_slots + 1):
                                if FileLoadable(slot, page=page):
                                    page_has_saves = True
                                    break
                            if page_has_saves:
                                max_page = page
                            else:
                                break
                        
                        # Если страница полная, добавляем следующую пустую
                        if current_page_full and max_page == current_page:
                            max_page = max_page + 1
                    
                    # Показываем страницы
                    for page_num in range(1, max_page + 1):
                        if page_num == current_page:
                            textbutton "[page_num]" action FilePage(page_num) style "page_num_current_button"
                        else:
                            textbutton "[page_num]" action FilePage(page_num) style "page_num_button"

                    # КНОПКА ">" - активна ТОЛЬКО если текущая страница ПОЛНОСТЬЮ ЗАПОЛНЕНА
                    if current_page_full:
                        textbutton _(">") action FilePageNext()
                    else:
                        textbutton _(">") action None sensitive False
                        
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