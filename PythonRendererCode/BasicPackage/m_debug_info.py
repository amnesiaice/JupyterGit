from enum import Enum


class LogLevel(Enum):
    NONE = ()
    ERROR = ()
    WARNING = ()
    DEBUG_INFO = ()
    INFO = ()
    ALL = ()


current_log_level = LogLevel.WARNING # log_level higher means more information


def debug_print(p_log_level, *args):
    if current_log_level.value < p_log_level.value:
        return
    elif current_log_level.value >= p_log_level.value:
        print("[%s]" % p_log_level.name),
        print("".join(str(i) for i in args))


def debug_img(img):
    for j in range(len(img)):
        for i in range(len(img[0])):
            if str(img[j][i]) == "[0.0, 0.0, 0.0, 1.0]":
                # debug_print(LogLevel.DEBUG_INFO, "color:", img[j][i])
                debug_print(LogLevel.DEBUG_INFO, "x:%s,y:%s" % (i, j))
