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


def debug_print_point(p_point, p_log_level=LogLevel.INFO):
    debug_print(p_log_level, "x:%d y:%d z:%d" % p_point.get_x(), p_point.get_y(), p_point.get_z())


def debug_img(img, b_blacklist_mode):
    l_filter = read_debug_point_filter()
    for j in range(len(img)):
        for i in range(len(img[0])):
            if (str(img[j][i]) in l_filter) ^ b_blacklist_mode: # blacklist all the listed point will not print
                # debug_print(LogLevel.DEBUG_INFO, "color:", img[j][i])
                debug_print(LogLevel.DEBUG_INFO, "x:%s,y:%s" % (i, j))
                debug_print(LogLevel.DEBUG_INFO, "point color:%s" % img[j][i])


def read_debug_point_filter():
    l_file = open("PythonRendererCode/BasicPackage/debug_point_info.txt")
    o_line_array = l_file.readlines()
    o_line_array = [line.strip('\n') for line in o_line_array]
    return o_line_array
