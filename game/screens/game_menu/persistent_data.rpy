init python:
    import uuid
    import datetime

    if not hasattr(persistent, "player_name") or persistent.player_name is None:
        persistent.player_name = ""
        
    def get_first_launch_date():

        if not hasattr(persistent, "first_launch_date") or persistent.first_launch_date is None:
            persistent.first_launch_date = datetime.datetime.now().strftime("%d.%m.%Y %H:%M")

        if not hasattr(persistent, "account_id") or persistent.account_id is None:
            persistent.account_id = str(uuid.uuid4())[:8].upper()

        renpy.save_persistent()

        return persistent.first_launch_date
    
