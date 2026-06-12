# game/chapters.rpy
default persistent.chapter_progress = {
    "chapter_1": {"unlocked": True, "completed": False, "name": "Анте приносит пойманный дух"},
    "chapter_2": {"unlocked": False, "completed": False, "name": "Ритуал"},
    "chapter_3": {"unlocked": False, "completed": False, "name": "разговор Анте и Пифона"},
    "chapter_4": {"unlocked": False, "completed": False, "name": "видение"},
    "chapter_5": {"unlocked": False, "completed": False, "name": "интерактив"},
    "chapter_6": {"unlocked": False, "completed": False, "name": "Ехидна приносит письмо"},
    "chapter_7": {"unlocked": False, "completed": False, "name": "поездка"},
    "chapter_8": {"unlocked": False, "completed": False, "name": "разговор Пифона и Ламии"},
}

init python:
    def complete_chapter(chapter_id):
        if chapter_id in persistent.chapter_progress:
            persistent.chapter_progress[chapter_id]["completed"] = True
            chapter_num = int(chapter_id.split("_")[1])
            next_chapter = f"chapter_{chapter_num + 1}"
            if next_chapter in persistent.chapter_progress:
                persistent.chapter_progress[next_chapter]["unlocked"] = True