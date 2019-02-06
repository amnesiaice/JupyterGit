from enum import Enum
from PythonRendererCode import config_warehouse


class LogLevel(Enum):
    NONE = 0
    ERROR = 1
    WARNING = 2
    DEBUG_INFO = 3
    INFO = 4
    ALL = 5


class DebugConfig:
    def __init__(self,
                 p_is_debug_enable=True,
                 p_current_log_level=LogLevel.ALL,
                 p_debug_filter_location="PythonRendererCode/PRDebugPackage/DebugFilter/",
                 p_debug_filter_name="debug_point_info.txt"
                 ):
        self.debug_enable = p_is_debug_enable
        self.current_log_level = p_current_log_level
        self.debug_filter_location = p_debug_filter_name
        self.debug_filter_name = p_debug_filter_location


class PRDebug:
    g_debug_enable = True

    def __init__(self,
                 p_is_debug_enable=True,
                 ):
        self.__read_debug_config()
        p_is_debug_enable = p_is_debug_enable and PRDebug.g_debug_enable
        if p_is_debug_enable:
            self.debug_enable = True
            self.current_log_level = LogLevel.ALL
            self.debug_filter_location = "PythonRendererCode/PRDebugPackage/DebugFilter/"
            self.debug_filter_name = "debug_point_info.txt"
            self.debug_info_img = []
            self.is_blacklist_mode = True
            self.__debug_filter_line = []
        else:
            self.debug_enable = False

    # ============================================================
    # set debug config function
    # ============================================================
    def set_debug_enable(self, p_debug_enable):
        self.debug_enable = p_debug_enable

    def set_current_log_level(self, p_current_log_level):
        self.current_log_level = p_current_log_level

    def set_filter_file_name(self, p_debug_filter_name):
        self.debug_filter_name = p_debug_filter_name

    def set_filter_file_path(self, p_debug_filter_location):
        self.debug_filter_location = p_debug_filter_location

    def set_debug_info_img(self, p_debug_info_img):
        self.debug_info_img = p_debug_info_img

    def set_blacklist_mode(self, p_is_blacklist_mode):
        self.is_blacklist_mode = p_is_blacklist_mode

    def set_debug_config(self,
                         p_debug_config
                         ):
        if p_debug_config.debug_enable:
            self.debug_enable = True
            self.current_log_level = p_debug_config.current_log_level
            self.debug_filter_location = p_debug_config.debug_filter_name
            self.debug_filter_name = p_debug_config.debug_filter_location
            self.debug_info_img = []
            self.__debug_filter_line = []
        else:
            self.debug_enable = False

    def get_debug_enable(self):
        return self.debug_enable and PRDebug.g_debug_enable

    # ============================================================
    # debug tool
    # ============================================================
    def debug_print(self, p_log_level, *args):
        if not self.get_debug_enable():
            return
        if self.current_log_level.value < p_log_level.value:
            return
        elif self.current_log_level.value >= p_log_level.value:
            print("[%s]" % p_log_level.name),
            print("".join(str(i) for i in args))

    def debug_print_point(self, p_point, p_log_level=LogLevel.INFO):
        if not self.get_debug_enable():
            return
        self.debug_print(p_log_level, "x:%d y:%d z:%d" % p_point.get_x(), p_point.get_y(), p_point.get_z())

    def debug_img(self):
        if not self.get_debug_enable():
            return
        self.__read_debug_point_filter()
        for j in range(len(self.debug_info_img)):
            for i in range(len(self.debug_info_img[0])):
                if (str(self.debug_info_img[j][i]) in self.__debug_filter_line) ^ self.is_blacklist_mode:
                    self.debug_print(LogLevel.DEBUG_INFO, "x:%s,y:%s" % (i, j))
                    self.debug_print(LogLevel.DEBUG_INFO, "point color:[%.2f, %.2f, %.2f, %.2f]" %
                                     (self.debug_info_img[j][i][0], self.debug_info_img[j][i][1],
                                      self.debug_info_img[j][i][2], self.debug_info_img[j][i][3])
                                     )

    # ============================================================
    # private function
    # ============================================================
    def __read_debug_point_filter(self):
        if not self.get_debug_enable():
            return
        l_file_name = self.debug_filter_location + self.debug_filter_name
        l_file = open(l_file_name)
        l_filter_file = l_file.readlines()
        l_filter_file = [line.strip('\n') for line in l_filter_file]
        # read is_blacklist
        if l_filter_file[0] == "blacklist":
            self.set_blacklist_mode(True)
        elif l_filter_file[0] == "whitelist":
            self.set_blacklist_mode(False)

        self.__debug_filter_line = l_filter_file[1:]
        l_file.close()

    @staticmethod
    def __read_debug_config():
        PRDebug.g_debug_enable = config_warehouse.g_debug_enable_config
