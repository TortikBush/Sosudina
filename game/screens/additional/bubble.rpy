################################################################################
## Пузырьковый экран
################################################################################

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left": {
        "window_background": Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding": 27,
    },
    "bottom_right": {
        "window_background": Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding": 27,
    },
    "top_left": {
        "window_background": Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding": 27,
    },
    "top_right": {
        "window_background": Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding": 27,
    },
    "thought": {
        "window_background": bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left": (0, 0, 0, 22),
    "bottom_right": (0, 0, 0, 22),
    "top_left": (0, 22, 0, 0),
    "top_right": (0, 22, 0, 0),
    "thought": (0, 0, 0, 0),
}

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