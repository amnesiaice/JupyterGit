from PythonRendererCode.BasicPackage import *


class Canvas:
    def __init__(self):
        self.width = 800.0
        self.height = 600.0
        self.back_ground_color_vector = m_color.Color.get_default_color()
        self.target = [[[]]]

    def init_canvas(self, p_width, p_height, p_color=m_color.Color.get_default_color()):
        # =================
        # prepare parameter
        # =================
        p_width = int(p_width)
        p_height = int(p_height)
        p_color = [float(i) for i in p_color]
        # =================
        # init canvas and related attribute
        # =================
        self.width = p_width
        self.height = p_height
        self.back_ground_color_vector = p_color
        # use this way to init 2-dim list to avoid shallow copy
        self.target = [[self.back_ground_color_vector for i in range(p_width)] for j in range(p_height)]

    def set_point(self, p_x, p_y, p_color):
        self.target[p_y][p_x] = p_color

    def set_point_buffer(self, p_point2_buffer):
        for i_point2 in p_point2_buffer:
            self.set_point(i_point2[0], i_point2[1], i_point2[2])
